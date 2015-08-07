import re

regex = re.compile('(\d+)')
print ('Numbers found: '+str(
	regex.findall('There were 55000 people there tonight. Or maybe 750000')))