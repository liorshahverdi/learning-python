pets = ['Zophie', 'Pooka', 'fat-tail']
print('Enter a pet name: ')
name = raw_input()
if name not in pets:
	print('I dont have a pet named '+ name)
else:
	print(name + ' is my pet.')