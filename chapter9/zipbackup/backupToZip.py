# backupToZip.py - Copies an entire folder and its contents into 
# a zip file whose filename increments.

import zipfile, os

def backupToZip(folder):
	# Backup the entire contents of a folder to a zipfile
	folder = os.path.abspath(folder) # make sure folder is absolute

	# Figure out the filename this code should use based on 
	# what files already exist.
	number = 1
	while True:
		zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFileName):
			break
		number += 1
	# Create the zip file
	print('Creating %s...' % (zipFileName))
	backupZip = zipfile.ZipFile(zipFileName, 'w')

	# Walk the entire folder tree and compress the files in each folder.
	for folderName, subfolders, filenames in os.walk(folder):
		print('Adding files in %s...' % (folderName))
		# Add the current folder to the zip file.
		backupZip.write(folderName)
		# Add all the files in this folder to the ZIP file
		for filename in filenames:
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue # don't backup the backup zip files
			backupZip.write(os.path.join(folderName, filename))
	backupZip.close()
	print('Done.')

backupToZip('.')