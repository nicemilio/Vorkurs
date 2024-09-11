alice = ['Bananen ', 'Brot', 'Schokolade ', 'Rotwein ']
bob = ['Bier', 'Bier', 'Chips ']
eve = ['Brot', 'Schokolade ', 'Chips ', 'Bier', 'Wasser ']

list = alice + bob + eve

shopping_list = {}

for item in list:
	if item in shopping_list:
		shopping_list[item] = shopping_list[item] + 1
	else:
		shopping_list [item] = 1

#print (shopping_list)

for key, value in shopping_list.items():
    print(key, value)
