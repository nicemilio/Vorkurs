import argparse

parser = argparse.ArgumentParser("Mit alten Griechen sieben")
parser.add_argument("--number", help="Optional: The upper limit for the returned prime numbers", type=int)
args = parser.parse_args()

def main():
	print (prim (args.number))

def prim (max):
	result = []
	for i in range (1, max + 1):
		if (isPrime (i)):
			result.append (i)
	return result

def isPrime (number):
	counter = 0
	for i in range (1, number + 1):
		if (number % i == 0):
			counter += 1
			if (counter > 1 and i != number):
				return False
			elif (i == number):
				return True

if __name__=="__main__":
   main()
