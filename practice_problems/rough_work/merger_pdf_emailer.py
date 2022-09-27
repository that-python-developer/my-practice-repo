import psycopg2
import smtplib

from pandas import read_sql, DataFrame
from datetime import date
from os import path as os_path, listdir as os_listdir
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from distutils.dir_util import copy_tree
from shutil import rmtree as shutil_rmtree
from PyPDF2 import PdfMerger


def archival_process():
    merged_pdf_source_folder = 'D:\\Tableau_AutoMailer\\merged_pdfs'
    merged_pdf_destination_folder = 'D:\\Tableau_AutoMailer\\Archival\\merged_pdf_archived'

    shutil_rmtree(merged_pdf_destination_folder)
    print('# ----------------------------- Old Archives Deleted --------------------------------------------- #\n')

    print('# --------------------------- Archival Process Started ------------------------------------------- #\n')

    copy_tree(merged_pdf_source_folder, merged_pdf_destination_folder)

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
    merged_pdf_files_path = 'D:\\Tableau_AutoMailer\\merged_pdfs'
    pdf_files = os_listdir(pdf_files_path)

    sender_email = "business.reports@innoviti.com"
    email_password = '$r!j@n@@tm@k'

    today_date = date.today()
    email_from = 'Innoviti Business Report'

    # ---------------------------------------- SMTP Connection with Server ---------------------------------------------

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        merchant_result_df = DataFrame(pdf_files, columns=['pdf_file_names'])
        merchant_result_df['merchant_code'] = merchant_result_df.pdf_file_names.apply(
            lambda x: x.split('.pdf')[0].split('_')[-1])
        merchant_result_df = merchant_result_df.groupby(['merchant_code'])['pdf_file_names'].apply(
            ','.join).reset_index()

        for index, row in merchant_result_df.iterrows():
            dashboard_name = merchant_code = row['merchant_code']
            pdf_file_path = os_path.join(merged_pdf_files_path, '{}.{}'.format(merchant_code, 'pdf'))
            pdfs = row['pdf_file_names'].split(',')
            merger = PdfMerger()
            for pdf in pdfs:
                merger.append(os_path.join(pdf_files_path, pdf))
            merger.write(pdf_file_path)
            merger.close()
            merged_file_name = pdf_file_path.split('\\')[-1]

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

                # ------------------- Attach PDF in the email ----------------------------------------------------------
                with open(pdf_file_path, 'rb') as pdf_attachment:
                    msg = MIMEBase('application', 'octet-stream')
                    msg.set_payload(pdf_attachment.read())
                    encoders.encode_base64(msg)
                    msg.add_header('Content-Disposition', "attachment; filename= %s" % merged_file_name)
                    msgRoot.attach(msg)

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
