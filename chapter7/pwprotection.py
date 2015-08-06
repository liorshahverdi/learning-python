import re

def validate(pw):
	if len(pw) >= 8:
		lower_regex = re.compile(r'[a-z]')
		if lower_regex.search(pw) is not None:
			upper_regex = re.compile(r'[A-Z]')
			if upper_regex.search(pw) is not None:
				num_regex = re.compile(r'[0-9]+')
				if num_regex.search(pw) is not None:
					print 'Valid!'
				else:
					print 'Needs to contain at least 1 digit.'
			else:
				print'No uppercase characters.'
		else:
			print 'No lowercase characters.'

print 'Enter a password: '
validate(str(raw_input()))