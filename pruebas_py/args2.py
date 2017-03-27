import sys

##la cantidad mínima de argumentos de 'sys.argv' es 1

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Incorrect number of parameters"

        file = sys.argv[1]
        action = sys.argv[2]

        if action == '-c':
            check(file)
        elif action == '-h':
            hide(file)
            print "The file is hidden"
        elif action == '-s':
            show(file)
            print "The file is not hidden now"
        else:
            print("Wrong parameter")
