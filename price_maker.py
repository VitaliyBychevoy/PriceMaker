import openpyxl

wb = openpyxl.reader.excel.load_workbook(filename='catalog.xlsx', data_only=True)

print(wb.sheetnames)


