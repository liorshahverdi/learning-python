# strip.py 
import re

def my_strip(text):
	temp = ''
	chararr = list(text)
	for i in range(1, len(text)):
		if chararr[i] != ' ':
			temp += chararr[i]
	print temp

print 'enter something'
my_strip(str(raw_input()))