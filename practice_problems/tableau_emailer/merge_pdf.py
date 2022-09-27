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


if __name__ == '__main__':
    # ---------------------------------------- Configuring File Paths --------------------------------------------------

    pdf_files_path = 'D:\\Tableau_AutoMailer\\pdf\\Merchant-Weekly-Dashboard'
    merged_pdf_files_path = 'D:\\Tableau_AutoMailer\\merged_pdfs'
    pdf_files = os_listdir(pdf_files_path)

    pdf_files_df = DataFrame(pdf_files, columns=['pdf_file_names'])
    pdf_files_df['code'] = pdf_files_df.pdf_file_names.apply(lambda x: x.split('.pdf')[0].split('_')[-1])
    pdf_files_df = pdf_files_df.groupby(['code'])['pdf_file_names'].apply(','.join).reset_index()

    for index, row in pdf_files_df.iterrows():
            dashboard_name = merchant_code = row['code']
            pdf_file_path = os_path.join(merged_pdf_files_path, '{}.{}'.format(merchant_code, 'pdf'))
            pdfs = row['pdf_file_names'].split(',')
            merger = PdfMerger()
            for pdf in pdfs:
                merger.append(os_path.join(pdf_files_path, pdf))
            merger.write(pdf_file_path)
            merger.close()
            merged_file_name = pdf_file_path.split('\\')[-1]
