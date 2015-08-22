'''
	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('example.xlsx')
	>>> type(wb)
	<class 'openpyxl.workbook.workbook.Workbook'>


	Getting Sheets from the Workbook
	----------------------------------------------------------------------------
	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('example.xlsx')
	>>> wb.get_sheet_names()
	['Sheet1', 'Sheet2', 'Sheet3']
	>>> sheet = wb.get_sheet_by_name('Sheet3')
	>>> sheet
	<Worksheet "Sheet3">
	>>> type(sheet) 
	<class 'openpyxl.worksheet.worksheet.Worksheet'>
	>>> sheet.title
	'Sheet3'
	>>> anotherSheet = wb.get_active_sheet()
	>>> anotherSheet
	<Worksheet "Sheet1">
	----------------------------------------------------------------------------


	Getting Cells from the Sheets
	----------------------------------------------------------------------------
	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('example.xlsx')
	>>> sheet = wb.get_sheet_by_name('Sheet1')
	>>> sheet['A1']
	<Cell Sheet1.A1>
	>>> sheet['A1'].value
	datetime.datetime(2015, 4, 5, 13, 34, 2)
	>>> c = sheet['B1']
	>>> c.value
	'Apples'
	>>> 'Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value
	'Row 1, Column B is Apples'
	>>> 'Cell ' + c.coordinate + ' is ' + c.value
	'Cell B1 is Apples'
	>>> sheet['C1'].value
	73
	----------------------------------------------------------------------------
	
'''