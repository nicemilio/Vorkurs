import random

def main():
	combination = [random.randint(1, 9) for _ in range(4)]
	user_input = []
	print (combination)
	while True:
		print ("Input your try")
		user_input = list(map(int, input()))
		if (user_input == combination):
			break
		true_numbers = 0
		almost_true_numbers = 0
		#Fraglich ob eine Nummer als fast richtig angegeben wird wenn sie schon richtig an der anderen Stelle steht
		for index, num in enumerate(user_input):
			if (num == combination[index]):
				true_numbers += 1
			elif num in combination:
	       			almost_true_numbers += 1
		print (f"Übereinstimmende Ziffern: {true_numbers}")
		print (f"Richtige Ziffern (allerdings an der falschen Position: {almost_true_numbers}")
	print ("Whoop whoop you found the right combination")

if __name__=="__main__":
   main()
