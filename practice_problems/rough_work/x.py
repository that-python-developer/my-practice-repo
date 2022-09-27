import psycopg2
import smtplib
import tabula

from pandas import read_sql
from datetime import date
from os import path as os_path, listdir as os_listdir
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from distutils.dir_util import copy_tree
from shutil import rmtree as shutil_rmtree


def convert_pdf_to_excel(pdfs_path, excels_path):
    print('# --------------------------- Excel Conversion Started ------------------------------------------- #\n')
    excel_files = [f for f in os_listdir(pdfs_path) if os_path.isfile(os_path.join(pdfs_path, f))]
    for excel in excel_files:
        try:
            df = tabula.read_pdf(os_path.join(pdfs_path, excel), pages=1)[0]
            df.to_excel(os_path.join(excels_path, '{}{}'.format(excel.split('.pdf')[0], '.xlsx')), index=False)
        except IndexError:
            print('--> Not able to convert the pdf - {}'.format(os_path.join(pdfs_path, excel)))
    print('\n# -------------------------- Excel Conversion Completed ------------------------------------------ #\n')


def archival_process():
    pdf_source_folder = 'D:\\Tableau_AutoMailer\\pdf'
    pdf_destination_folder = 'D:\\Tableau_AutoMailer\\Archival\\pdf_archived'

    excel_source_folder = 'D:\\Tableau_AutoMailer\\excel'
    excel_destination_folder = 'D:\\Tableau_AutoMailer\\Archival\\excel_archived'

    img_source_folder = 'D:\\Tableau_AutoMailer\\img'
    img_destination_folder = 'D:\\Tableau_AutoMailer\\Archival\\img_archived'

    shutil_rmtree(pdf_destination_folder)
    shutil_rmtree(excel_destination_folder)
    shutil_rmtree(img_destination_folder)
    print('# ----------------------------- Old Archives Deleted --------------------------------------------- #\n')

    print('# --------------------------- Archival Process Started ------------------------------------------- #\n')

    copy_tree(pdf_source_folder, pdf_destination_folder)

    copy_tree(excel_source_folder, excel_destination_folder)

    copy_tree(img_source_folder, img_destination_folder)

    print('# -------------------------- Archival Process Completed ------------------------------------------ #\n')


if __name__ == '__main__':

    db_username = 'pentaho'
    db_password = 'pentaho'

    # db_name = 'edw_prod'
    # db_host = '172.25.185.16'
    # db_port = '5432'

    db_name = 'edw_dev'
    db_host = '124.153.107.29'
    db_port = '55432'

    # --------------------------------------- Establishing DB connection -----------------------------------------------
    db_connection = psycopg2.connect(
        database=db_name,
        user=db_username,
        password=db_password,
        host=db_host,
        port=db_port
    )
    print('Connection to Development - Successful\n')

    query = """
        select 
            merchant_code,
            merchant_name,
            user_id,
            user_name,
            user_email,
            refresh_date
        from edw_tab.reports_to_emails
        where is_active is true
    """
    email_df = read_sql(query, db_connection)

    # ---------------------------------------- Configuring File Paths --------------------------------------------------

    pdf_files_path = 'D:\\Tableau_AutoMailer\\pdf'
    img_files_path = 'D:\\Tableau_AutoMailer\\img'
    excel_files_path = 'D:\\Tableau_AutoMailer\\excel'
    pdf_files = os_listdir(pdf_files_path)
    # img_files = os_listdir(img_files_path)
    # excel_files = os_listdir(excel_files_path)

    convert_pdf_to_excel(pdf_files_path, excel_files_path)

    sender_email = "business.reports@innoviti.com"
    email_password = '$r!j@n@@tm@k'

    today_date = date.today()
    email_from = 'Innoviti Business Report'

    # ---------------------------------------- SMTP Connection with Server ---------------------------------------------

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        for pdf_file in pdf_files:
            dashboard_name = ''.join(pdf_file.split('.pdf')[0].split('_')[:-1])
            merchant_code = pdf_file.split('.pdf')[0].split('_')[-1]
            img_file = '{}{}'.format(pdf_file.split('.pdf')[0], '.png')
            excel_file = '{}{}'.format(pdf_file.split('.pdf')[0], '.xlsx')

            # ------------------- Checking if the mail id for a merchant code is present in DB -------------------------
            users_df = email_df[email_df['merchant_code'] == merchant_code]
            if users_df.empty:
                print('** WARN ** Could not find the mail id in DB for merchant_code : %s' % merchant_code)
                continue
            else:
                users = users_df['user_email'].iloc[0].split(',')

            for user in users:
                # -------------------------------------- Set variables -------------------------------------------------
                user_email = user
                refresh_date = users_df['refresh_date'].iloc[0]
                email_subject = '{dashboard_name} - Weekly Report {today_date}'.format(
                    dashboard_name=dashboard_name,
                    today_date=today_date
                )
                email_body = """
                    <br>
                    Dear User,
                    <br>
                    Pls find attached for {refresh_date}
                    <br>
                """.format(refresh_date=refresh_date)

                # ------------------- Create the root message and fill in To, From and Subject headers -----------------
                msgRoot = MIMEMultipart('related')
                msgRoot['From'] = email_from
                msgRoot['Subject'] = email_subject
                msgRoot['To'] = user_email
                # msgRoot.preamble = 'This is a multipart message in MIME format.'

                msgAlternative = MIMEMultipart('alternative')
                msgRoot.attach(msgAlternative)

                # msgText = MIMEText('This is the alternative plain text message.')
                # msgAlternative.attach(msgText)

                # ------------------- Embed image in the email body ----------------------------------------------------
                msgText = MIMEText(
                    """
                        {email_body}
                        <br>
                        <img src="cid:image1">
                        <br>
                    """.format(email_body=email_body),
                    'html'
                )
                msgAlternative.attach(msgText)

                try:
                    with open(os_path.join(img_files_path, img_file), 'rb') as img:
                        msgImage = MIMEImage(img.read())
                        msgImage.add_header('Content-ID', '<image1>')
                        msgImage.add_header('Content-Disposition', 'inline', filename=merchant_code)
                        msgRoot.attach(msgImage)

                except FileNotFoundError as t:
                    pass

                # ------------------- Attach PDF in the email ----------------------------------------------------------
                with open(os_path.join(pdf_files_path, pdf_file), 'rb') as pdf_attachment:
                    msg = MIMEBase('application', 'octet-stream')
                    msg.set_payload(pdf_attachment.read())
                    encoders.encode_base64(msg)
                    msg.add_header('Content-Disposition', "attachment; filename= %s" % pdf_file)
                    msgRoot.attach(msg)

                # ------------------- Attach Excel in the email --------------------------------------------------------
                try:
                    with open(os_path.join(excel_files_path, excel_file), 'rb') as excel_attachment:
                        msg = MIMEBase('application', 'octet-stream')
                        msg.set_payload(excel_attachment.read())
                        encoders.encode_base64(msg)
                        msg.add_header('Content-Disposition', "attachment; filename= %s" % excel_file)
                        msgRoot.attach(msg)
                except FileNotFoundError as t:
                    pass

                # ------------------- Send email -----------------------------------------------------------------------
                server.login(sender_email, email_password)
                server.sendmail(sender_email, user_email, msgRoot.as_string())
                print(
                    '--> {dashboard_name} mailed to mail_id {user_email} whose merchant_code is {merchant_code}'.format(
                        dashboard_name=dashboard_name,
                        user_email=user,
                        merchant_code=merchant_code
                    )
                )
    print('\nAll email sent.')

    archival_process()
