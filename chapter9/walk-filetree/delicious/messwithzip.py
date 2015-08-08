import zipfile, os

exampleZip = zipfile.ZipFile('cats.zip')
print 'Files in this .zip file: '+str(exampleZip.namelist())

spamInfo = exampleZip.getinfo('cats/spam.txt')
print 'File size: '+str(spamInfo.file_size)
print 'Compress size: '+str(spamInfo.compress_size)
print 'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))

exampleZip.close()