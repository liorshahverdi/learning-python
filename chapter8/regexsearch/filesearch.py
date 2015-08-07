import sys, os, re

print 'This program will search through all files in this directory for a match\nto the regex that you will provide.'
print 'Enter a regex'
regex_str = str(raw_input())
regex = re.compile(regex_str)
filenames = os.listdir('.')
for filename in filenames:
	if filename.endswith('.txt'):
		# Open the file
		myfile = open(filename, 'r')
		text_lines = myfile.readlines()
		matched_list = regex.findall(regex_str)
		for match in matched_list:
			print match