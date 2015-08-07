import sys, os, re

print 'This program will search through all files in this directory for a match\nto the regex that you will provide.'
print 'Enter a regex'
regex_str = str(raw_input())
myregex = re.compile(regex_str)
filenames = os.listdir('.')
matches = []
for filename in filenames:
	if filename.endswith('.txt'):
		# Open the file
		myfile = open(filename, 'r')
		# Extract the filetext as a list of string
		text_lines = myfile.readlines()
		#iterate through each line
		for line in text_lines:
			#extract the words in the line
			words = line.split()
			#iterate through the words in the line
			for word in words:
				#word is a match, add it to list of matches
				if myregex.search(word) is not None:
					mo = myregex.search(word)
					matches.append(mo.group())

for match in matches:
	print match