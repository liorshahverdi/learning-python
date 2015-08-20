
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

	Other Syntax
	----------------------------------------------------------------------------
	>>> sheet.cell(row=1, column=2)
	<Cell Sheet1.B1>
	>>> sheet.cell(row=1, column=2).value
	'Apples'
	>>> for i in range(1, 8, 2):
	        print(i, sheet.cell(row=i, column=2).value)

	1 Apples
	3 Pears
	5 Apples
	7 Strawberries
	---------------------------------------------------------------------------

	---------------------------------------------------------------------------
	You can determine the size of the sheet with the Worksheet object's
	get_highest_row() and get_highest_column() methods. 
	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('example.xlsx')
	>>> sheet = wb.get_sheet_by_name('Sheet1')
	>>> sheet.get_highest_row()
	7
	>>> sheet.get_highest_column()
	3
	---------------------------------------------------------------------------


	GETTING ROWS AND COLUMNS FROM THE SHEETS
	---------------------------------------------------------------------------
	 >>> import openpyxl
   >>> wb = openpyxl.load_workbook('example.xlsx')
   >>> sheet = wb.get_sheet_by_name('Sheet1')
   >>> tuple(sheet['A1':'C3'])
   ((<Cell Sheet1.A1>, <Cell Sheet1.B1>, <Cell Sheet1.C1>), (<Cell Sheet1.A2>,
   <Cell Sheet1.B2>, <Cell Sheet1.C2>), (<Cell Sheet1.A3>, <Cell Sheet1.B3>,
   <Cell Sheet1.C3>))
➊ >>> for rowOfCellObjects in sheet['A1':'C3']:
➋         for cellObj in rowOfCellObjects:
               print(cellObj.coordinate, cellObj.value)
           print('--- END OF ROW ---')
   A1 2015-04-05 13:34:02
   B1 Apples
   C1 73
   --- END OF ROW ---
   A2 2015-04-05 03:41:23
   B2 Cherries
   C2 85
   --- END OF ROW ---
   A3 2015-04-06 12:46:51
   B3 Pears
   C3 14
   --- END OF ROW ---
   	---------------------------------------------------------------------------

   	---------------------------------------------------------------------------
   	REVIEW
   	As a quick review, here’s a rundown of all the functions, methods, and data types involved in reading a cell out of a spreadsheet file:
	1. Import the openpyxl module.
	2. Call the openpyxl.load_workbook() function.
	3. Get a Workbook object.
	4. Call the get_active_sheet() or get_sheet_by_name() workbook method.
	5. Get a Worksheet object.
	6. Use indexing or the cell() sheet method with row and column keyword arguments.
	7. Get a Cell object.
	8. Read the Cell object’s value attribute.
   	---------------------------------------------------------------------------