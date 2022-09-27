from pandas import read_csv
from os import path as os_path, listdir as os_listdir, remove as os_remove
from os.path import splitext


print('# ------------------------------- Start - Deleting empty csv and pdf ---------------------------------------- #')

csv_cross_tab_folder_location = 'D:\\Tableau_AutoMailer\\csv\\Merchant-Weekly-Dashboard\\crosstab'
csv_non_cross_tab_folder_location = 'D:\\Tableau_AutoMailer\\csv\\Merchant-Weekly-Dashboard\\noncrosstab'
pdf_folder_location = 'D:\\Tableau_AutoMailer\\pdf\\Merchant-Weekly-Dashboard'

csv_cross_tab_file_list = os_listdir(csv_cross_tab_folder_location)

for file in csv_cross_tab_file_list:
    csv_file_location = os_path.join(csv_cross_tab_folder_location, file)
    df = read_csv(csv_file_location)
    if df.empty:
        pdf_file_location = os_path.join(pdf_folder_location, f'{splitext(file)[0]}.pdf')
        os_remove(pdf_file_location)
        os_remove(csv_file_location)

csv_non_cross_tab_file_list = os_listdir(csv_non_cross_tab_folder_location)
for file in csv_non_cross_tab_file_list:
    csv_file_location = os_path.join(csv_non_cross_tab_folder_location, file)
    df = read_csv(csv_file_location)
    if df.empty:
        pdf_file_location = os_path.join(pdf_folder_location, f'{splitext(file)[0]}.pdf')
        os_remove(pdf_file_location)
        os_remove(csv_file_location)

print('# ------------------------------- Finish - Deleted empty csv and pdf ---------------------------------------- #')
