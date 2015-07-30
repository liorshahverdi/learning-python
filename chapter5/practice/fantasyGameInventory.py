#inventory.py
def displayInventory(inventory):
	sum = 0
	print('Inventory:')
	for k, v in inventory.items():
		print v, k
		sum += v

	print 'Total number of items: ', sum

def addToInventory(inventory, addedItems):
	for item in addedItems:
		if item in inventory.keys():
			inventory[item] += 1
		else:
			inventory.setdefault(item, 1)
	

inv = { 'gold coin': 42, 'rope':1 }
displayInventory(inv)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#inv = addToInventory(inv, dragonLoot)
addToInventory(inv, dragonLoot)
displayInventory(inv)