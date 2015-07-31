def myprintmethod(name):
	for i in name:
		print('***'+i+'***')

print('What is your name? ', sep='')
name = str(raw_input())
myprintmethod(name)