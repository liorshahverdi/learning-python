import zipfile, os

print('Enter the name of the zipfile:')
userinput = str(raw_input())

ourfile = zipfile.ZipFile(userinput)
ourfile.extractall()
ourfile.close()