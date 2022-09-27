import psycopg2
import smtplib
import traceback

from pandas import read_sql
from datetime import date
from os import path as os_path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from distutils.dir_util import copy_tree
from shutil import rmtree as shutil_rmtree


def archival_process():
    merged_pdf_source_folder = 'D:\\Tableau_AutoMailer\\merged_pdfs'
    merged_pdf_destination_folder = 'D:\\Tableau_AutoMailer\\Archival\\merged_pdf_archived'
    merged_excel_source_folder = 'D:\\Tableau_AutoMailer\\merged_excel'
    merged_excel_destination_folder = 'D:\\Tableau_AutoMailer\\Archival\\merged_excel_archived'

    shutil_rmtree(merged_pdf_destination_folder)
    shutil_rmtree(merged_excel_destination_folder)
    print('# ----------------------------- Old Archives Deleted --------------------------------------------- #\n')

    print('# --------------------------- Archival Process Started ------------------------------------------- #\n')

    copy_tree(merged_pdf_source_folder, merged_pdf_destination_folder)
    copy_tree(merged_excel_source_folder, merged_excel_destination_folder)

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
            code,
            dashboard_name,
            user_email,
            refresh_date
        from edw_tab.reports_to_emails
        where is_active is true
    """
    email_df = read_sql(query, db_connection)

    # ---------------------------------------- Configuring File Paths --------------------------------------------------

    pdf_files_path = 'D:\\Tableau_AutoMailer\\merged_pdfs'
    excel_files_path = 'D:\\Tableau_AutoMailer\\merged_excel'

    sender_email = "business.reports@innoviti.com"
    email_password = '$r!j@n@@tm@k'

    today_date = date.today()
    email_from = 'Innoviti Business Report'

    # ---------------------------------------- SMTP Connection with Server ---------------------------------------------

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        for index, row in email_df.iterrows():
            pdf_file = os_path.join(pdf_files_path, f"{row['code']}.pdf")
            excel_file = os_path.join(excel_files_path, f"{row['code']}.xlsx")

            try:
                users = row['user_email'].split(',')
            except AttributeError as e:
                trace_back = ''.join(traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__))
                trace_back = trace_back.replace('\'', '"')
                log_msg = f"""
                    INSERT INTO edw_tab.admin_email_log_history (created_date, log_message, err_message)
                    VALUES(now(), 'No email found in DB for code : {row['code']}', '{trace_back}');
                """
                db_connection.cursor().execute(log_msg)
                db_connection.commit()
                continue

            for user in users:
                # -------------------------------------- Set variables -------------------------------------------------
                user_email = user
                refresh_date = row['refresh_date']
                email_subject = '{dashboard_name} - Weekly Report {today_date}'.format(
                    dashboard_name=row['dashboard_name'],
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

                # ------------------- Check if PDF exists and attach in email ------------------------------------------
                try:
                    with open(pdf_file, 'rb') as pdf_attachment:
                        msg = MIMEBase('application', 'octet-stream')
                        msg.set_payload(pdf_attachment.read())
                        encoders.encode_base64(msg)
                        msg.add_header('Content-Disposition', "attachment; filename= %s" % f"{row['code']}.pdf")
                        msgRoot.attach(msg)
                except FileNotFoundError as e:
                    trace_back = ''.join(traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__))
                    trace_back = trace_back.replace('\'', '"')
                    log_msg = f"""
                        INSERT INTO edw_tab.admin_email_log_history (created_date, log_message, err_message)
                        VALUES(now(), 'No PDF file present for group code {row['code']}', '{trace_back}');
                    """
                    db_connection.cursor().execute(log_msg)
                    db_connection.commit()

                # ------------------- Check if Excel exists and attach in email ----------------------------------------
                try:
                    with open(os_path.join(excel_files_path, excel_file), 'rb') as excel_attachment:
                        msg = MIMEBase('application', 'octet-stream')
                        msg.set_payload(excel_attachment.read())
                        encoders.encode_base64(msg)
                        msg.add_header('Content-Disposition', "attachment; filename= %s" % f"{row['code']}.xlsx")
                        msgRoot.attach(msg)
                except FileNotFoundError as e:
                    trace_back = ''.join(traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__))
                    trace_back = trace_back.replace('\'', '"')
                    log_msg = f"""
                        INSERT INTO edw_tab.admin_email_log_history (created_date, log_message, err_message)
                        VALUES(now(), 'No Excel file present for group code {row['code']}', '{trace_back}');
                    """
                    db_connection.cursor().execute(log_msg)
                    db_connection.commit()

                # ------------------- Send email -----------------------------------------------------------------------
                server.login(sender_email, email_password)
                server.sendmail(sender_email, user_email, msgRoot.as_string())
                print(
                    '--> {dashboard_name} mailed to mail_id {user_email} whose code is {code}'.format(
                        dashboard_name=row['dashboard_name'],
                        user_email=user,
                        code=row['code']
                    )
                )
    print('\nAll email sent.')

    archival_process()
