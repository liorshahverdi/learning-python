import shelve
shelfFile = shelve.open('mydata')
dogs = ['Jamie', 'Tucker', 'Max']
shelfFile['dogs'] = dogs
shelfFile.close()