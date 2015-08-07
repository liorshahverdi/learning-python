
infile = open('text.txt', 'r')
lines = infile.read()
words = lines.split()
#print words
for i in range(len(words)):
	if words[i] == 'ADJECTIVE':
		print 'Enter an adjective:'
		adj = str(raw_input())
		words[i] = adj
	elif words[i] == 'NOUN':
		print 'Enter a noun:'
		noun = str(raw_input())
		words[i] = noun
	elif words[i] == 'VERB':
		print 'Enter a verb:'
		verb = str(raw_input())
		words[i] = verb
infile.close()
outputfile = open('text.txt', 'w')
outstring = ''
for i in range(len(words)):
	if i != len(words) - 1:	
		outstring += words[i]+' '
	else:
		outstring += words[i]
outputfile.write(outstring)
outputfile.close()