import os

x = str(os.path.getsize('.'))
print 'Size of current working directory: '+x
y = str(os.listdir('.'))
print 'Files in current working directory: '+y

totalSize = 0
for filename in os.listdir('.'):
	totalSize += os.path.getsize(os.path.join('.', filename))

print 'totalSize: '+str(totalSize)