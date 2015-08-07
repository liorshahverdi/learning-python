import zipfile, os

print('Enter the name of the zipfile:')
userinput = str(raw_input())

ourfile = zipfile.ZipFile(userinput)
ourfile.extractall()
ourfile.close()

'''
>>> import zipfile
>>> newZip = zipfile.ZipFile('new.zip', 'w')
>>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
>>> newZip.close()
'''