import requests
print 'Enter the URL you would like to scrape please.'
res = requests.get(str(raw_input()))
res.raise_for_status()
for chunk in res.iter_content(100000):
	print chunk

print'Would you like to write this page to a file? (y/n)'
answer = str(raw_input())
if answer == 'y':
	print'Enter a filename'
	newfilename = str(raw_input())
	newFile = open(newfilename, 'wb')
	for chnk in res.iter_content(100000):
		newFile.write(chnk)

	newFile.close()
	print newfilename+' has been successfully created in the current working directory.'