import re

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
newstr = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print newstr