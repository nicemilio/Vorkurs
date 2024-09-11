import random

dict = {}

for key in range (1, 11):
	dict [key] = {}
	for value in range (1, 11):
		result = key * value
		dict [key][value] = result

first = random.randint (1, 10)
second = random.randint (1, 10)
print (f"What is {first} times {second}?") 

input = int(input ())

if input != dict [first][second]:
	print ("Moron")
else:
	print ("Not a moron")
