'''
	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('example.xlsx')
	>>> type(wb)
	<class 'openpyxl.workbook.workbook.Workbook'>


	Getting Sheets from the Workbook

	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('example.xlsx')
	>>> wb.get_sheet_names()
	['Sheet1', 'Sheet2', 'Sheet3']
	>>> sheet = wb.get_sheet_by_name('Sheet3')
	>>> sheet
	<Worksheet "Sheet3">
	>>> type(sheet) <class 'openpyxl.worksheet.worksheet.Worksheet'>
	>>> sheet.title
	'Sheet3'
	>>> anotherSheet = wb.get_active_sheet()
	>>> anotherSheet
	<Worksheet "Sheet1">

'''