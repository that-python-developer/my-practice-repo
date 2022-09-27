import os


def remove_files(file_path):
    file_list = [f for f in os.listdir(file_path)]
    for f in file_list:
        os.remove(os.path.join(file_path, f))


pdf_source_folder = 'D:\\Tableau_AutoMailer\\pdf'

excel_source_folder = 'D:\\Tableau_AutoMailer\\excel'

img_source_folder = 'D:\\Tableau_AutoMailer\\img'

merged_pdf_source_folder = 'D:\\Tableau_AutoMailer\\merged_pdfs'

print('# ----------------------------- Deleting All PDF, excel, img, merged PDF ---------------------------------- #\n')

remove_files(pdf_source_folder)
remove_files(excel_source_folder)
remove_files(img_source_folder)
remove_files(merged_pdf_source_folder)

print('# ----------------------------- Deleted All PDF, excel, img, merged PDF ----------------------------------- #\n')
