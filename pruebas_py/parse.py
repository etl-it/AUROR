import argparse

parser=argparse.ArgumentParser()
parser.parse_args()

##Specify what kind of command-line options the program will accept
parser.add_argument("echo", help="echo the string you use here") #naming it "echo"
args = parser.parse_args()   #returns data from the options specified(echo)
print(args.echo)

##argparse treats the options we give as a string
