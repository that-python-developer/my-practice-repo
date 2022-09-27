import os


def remove_files(file_path):
    file_list = [f for f in os.listdir(file_path)]
    for f in file_list:
        os.remove(os.path.join(file_path, f))


pdf_source_folder = 'D:\\Tableau_AutoMailer\\pdf\\Merchant-Weekly-Dashboard'

csv_crosstab_source_folder = 'D:\\Tableau_AutoMailer\\csv\\Merchant-Weekly-Dashboard\\crosstab'

csv_non_crosstab_source_folder = 'D:\\Tableau_AutoMailer\\csv\\Merchant-Weekly-Dashboard\\crosstab'

csv_header_source_folder = 'D:\\Tableau_AutoMailer\\csv\\Merchant-Weekly-Dashboard\\header'

excel_source_folder = 'D:\\Tableau_AutoMailer\\excel\\Merchant-Weekly-Dashboard'

img_source_folder = 'D:\\Tableau_AutoMailer\\img\\Merchant-Weekly-Dashboard'

merged_excel_source_folder = 'D:\\Tableau_AutoMailer\\merged_excel'

merged_pdf_source_folder = 'D:\\Tableau_AutoMailer\\merged_pdfs'

print('# ----------------------------- Deleting All PDF, excel, img, merged PDF ---------------------------------- #\n')

remove_files(pdf_source_folder)
remove_files(csv_crosstab_source_folder)
remove_files(csv_non_crosstab_source_folder)
remove_files(csv_header_source_folder)
remove_files(excel_source_folder)
remove_files(img_source_folder)
remove_files(merged_excel_source_folder)
remove_files(merged_pdf_source_folder)

print('# ----------------------------- Deleted All PDF, excel, img, merged PDF ----------------------------------- #\n')
