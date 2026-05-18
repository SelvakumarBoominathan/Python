# Test file to read data from excel sheet using openpyxl library

import openpyxl

work_book = openpyxl.load_workbook(
    "C:\\Users\\selva\\OneDrive\\Desktop\\testfilepandas\\New Microsoft Excel Worksheet.xlsx")

sheet_obj = work_book['Answers']

print(sheet_obj['B2'].value)


# initial Setup
