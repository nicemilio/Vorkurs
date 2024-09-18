import argparse

parser = argparse.ArgumentParser("Fliesenleger des Königs")
parser.add_argument("rows", help="The nunber of rows you want to print", type=int)
parser.add_argument("columns", help="The nunber of columns you want to print", type=int)
args = parser.parse_args()

row = "#o"
for i in range (0, args.rows):
	if (i % 2 == 0):
		rowString = row * int(args.columns / 2)
		if (args.columns % 2 != 0):
			rowString =  row + rowString[:-1]
		print (rowString)
	else:
		rowString = row[::-1] * int(args.columns / 2)
		if (args.columns % 2 != 0):
			rowString =  row[::-1] + rowString[:-1]
		print (rowString)