import argparse

parser = argparse.ArgumentParser("Jäger des Verlorenen Tages")
parser.add_argument("year", help="The year you want to check for a leap-year", type=int)
args = parser.parse_args()

if ((args.year % 4 == 0 and args.year % 100 != 0) or args.year % 400 == 0):
	print ("Leap year")
else:
	print ("No leap year")
