#fun with phone numbers
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is is 415-555-4242')
print('Group 1: '+mo.group(1))
print('Group 2: '+mo.group(2))
print('Group 0: '+mo.group(0))
print('group(): '+mo.group())