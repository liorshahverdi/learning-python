import shelve

shelfFile = shelve.open('mydata')
print str(type(shelfFile))
print shelfFile['dogs']
shelfFile.close()