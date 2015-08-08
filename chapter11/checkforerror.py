import requests
res = requests.get('http://inventwithpython.com/page_that_doesnt_exist')
try:
	res.raise_for_status()
except Exception as exc:
	print('There was a problem: %s' % (exc))

'''
Always call raise_for_status() after calling requests.get(). 
You want to be sure that the download has actually worked 
before your program continues.
'''