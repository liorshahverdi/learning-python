#regex.py
import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('My number is 415-555-2442.')
print('Phone number found: '+mo.group())

if mo.group() == '415-555-2442':
	print True