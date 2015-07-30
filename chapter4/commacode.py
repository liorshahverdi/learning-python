def concat(passedList):
	temp = ''
	i = 0
	if len(passedList) == 1:
		return passedList[0]
	else:
		for str in passedList:
			if i != len(passedList) - 1:
				temp += str+','
			else:
				temp += ' and ' +str
			i += 1
		return temp


list = ['apples', 'bananas', 'tofu', 'cats']
#list = ['apples']
print(concat(list))