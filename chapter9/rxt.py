import os
for filename in os.listdir():
	if filename.endswith('.rxt'):
		#os.unlink(filename)
		print(filename)

'''
For le interpreter:

>>> import send2trash
>>> baconFile = open('bacon.txt', 'a') # creates the file
>>> baconFile.write('Bacon is not a vegetable.')
>>> baconFile.close()
>>> send2trash.send2trash('bacon.txt')

# There should now be a file called bacon.txt in the recylce bin rather than being
# permanently deleted. Much better!

'''