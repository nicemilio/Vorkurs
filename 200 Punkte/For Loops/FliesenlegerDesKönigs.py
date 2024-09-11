import argparse

parser = argparse.ArgumentParser("Fliesenleger des Königs")
parser.add_argument("rows", help="The nunber of rows you want to print", type=int)
args = parser.parse_args()

row = "#o#o#o#o"

for i in range (0, args.rows):
	if (i % 2 == 0):
		print (row)
	else:
		print(row[::-1])
