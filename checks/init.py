import sys, getopt

def main(argv):
    conffile = ''
    outputfile = ''

    try:
        opts,args = getopt.getopt(argv, "hi:o", ["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            conffile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-d", "--ifile"):
            conffile = /tmp/conf_default.cfg
        elif opt in ("-d", "--ofile"):
            outputfile = /tmp/conf_default.cfg
        end if
