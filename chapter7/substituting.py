import re


print 'Agent Alice gave the secret documents to Agent Bob.'
namesRegex = re.compile(r'Agent \w+')
newstr = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print newstr