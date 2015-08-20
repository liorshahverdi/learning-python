CREATING AND SAVING EXCEL DOCUMENTS
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> wb.get_sheet_names()
['Sheet']
>>> sheet = wb.get_active_sheet()
>>> sheet.title
'Sheet'
>>> sheet.title = 'Spam Bacon Eggs Sheet'
>>> wb.get_sheet_names()
['Spam Bacon Eggs Sheet']

------------------------------------------------------------------------------------

Any time you modify the Workbook object or its sheets and cells, the spreadsheet file will not be saved until you call the save() workbook method. Enter the following into the interactive shell (with example.xlsx in the current working directory):

> import openpyxl
> wb = openpyxl.load_workbook('example.xlsx')
> sheet = wb.get_active_sheet()
> sheet.title = 'Spam Spam Spam'
> wb.save('example_copy.xlsx')
------------------------------------------------------------------------------------


RENAMING !!!
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_active_sheet()
>>> sheet.title = 'Spam Spam Spam'
>>> wb.save('example_copy.xlsx')