# This program finds emails and addresses on the clipboard.

import re

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?				# area code
	(\s|-|\.)?						# separator
	\d{3}							# first 3 digits
	(\s|-|\.)						# separator
	\d{4}							# last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})?	# extension
	)''', re.VERBOSE)

#TODO : Create email regex
emailRegex = re.compile('[^@]+@[^@]+\.[^@]+')

#TODO : Find matches in clipboard text.
print'Enter a filename. '
filename = str(raw_input())
matches = []
with open(filename, 'r') as f:
	for line in f: