import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square",help="display a square of a given number",type=int)
parser.add_argument("-v","--verbose", help="increase output verbosity",action="store_true")
args = parser.parse_args()

if args.square:
    print(args.square**2)
elif args.verbose:
    print("verbosity turned on")
