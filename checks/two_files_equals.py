import time
import re
import os
import getopt
import sys

outfile = open("/usr/lab/alum/0330717/AUROR/salida.txt","w")

file1 = ''
file1 = ''

#infile1 = open('/usr/lab/alum/0330717/AUROR/prueba.txt', 'r')
#infile2 = open('/usr/lab/alum/0330717/AUROR/prueba_no_guay.txt', 'r')

def identify(file):
    dtype = ''
    comment_init    = ''
    comment_end     = ''
    other_comment   = ''
    properties = ''

    possible_extensions = ['bz2','gz','tar','tbz','tgz','zip',
                           'au', 'gif','html','htm','jpg','pdf','png','ps','txt','wav','xpm',
                           'conf', 'lock', 'rpm'
                           'c','cpp','h','o','pl','py','so','sh','tcl'
                           'doc','docx']
    extension = file.split('.')[-1]
    print(extension)

    if extension in possible_extensions:
        if extension == 'bz2' or extension == 'gz' or extension == 'tar' or extension == 'tbz' or extension == 'tgz' or extension == 'zip':
                dtype = "COMPRESSED"
                comment_init    = None
                comment_end     = None
                other_comment   = None

        elif extension == 'conf' or extension == 'lock' or extension == 'rpm':
                dtype = "SYSTEM_FILE"
                comment_init    = None
                comment_end     = None
                other_comment   = None

        elif extension == 'au' or extension == 'wav':
                dtype = "AUDIO"
                comment_init    = None
                comment_end     = None
                other_comment   = None

        elif extension == 'gif' or extension == 'jpg' or extension == 'png' or extension == 'xpm':
                dtype = "IMAGE"
                comment_init    = None
                comment_end     = None
                other_comment   = None

        elif extension == 'html' or extension == 'htm':
                dtype = "HMTL"
                comment_init    = "<!--'" #begin comment
                comment_end     = "'-->'" #close comment
                other_comment   = None

        elif extension == 'pdf':
                dtype = "PDF"
                comment_init    = None
                comment_end     = None
                other_comment   = None

        elif extension == 'ps':
                dtype = "POSTSCRIPT"
                comment_init    = None
                comment_end     = None
                other_comment   = "%"

        elif extension == 'txt':
                dtype = "TXT"
                comment_init    = None
                comment_end     = None
                other_comment   = None

        elif extension == 'c' or extension == 'h':
                dtype = "SCRIPT_C"
                comment_init    = "/\*"
                comment_end     = "\*/"
                other_comment   = '//'

        elif extension == 'cpp':
                dtype = "SCRIPT_C_PLUS"
                comment_init    = "/\*"
                comment_end     = "\*/"
                other_comment   = "//"

        elif extension == 'o':
                dtype = "OBJECT_C"
                comment_init    = None
                comment_end     = None
                other_comment   = None

        elif extension == 'py':
                dtype = "SCRIPT_PYTHON"
                comment_init    = "'''"
                comment_end     = "'''"
                other_comment   = "#"


        elif extension == 'pl':
                dtype = SCRIPT_PERL
                comment_init    = None
                comment_end     = None
                other_comment   = "#" #contemplar la posibilidad de ser la linea de path

        elif extension == '.so':
                dtype = "LIBRARY_FILE"
                comment_init    = None
                comment_end     = None
                other_comment   = None

        elif extension == '.sh':
                dtype = "SCRIPT_SHELL"
                comment_init    = None
                comment_end     = None
                other_comment   = "#"

        elif extension == '.tcl':
                dtype = "SCRIPT_TCL"
                comment_init    = None
                comment_end     = None
                other_comment   = "#"

        elif extension == "doc" or extension == "docx":
                dtype = "DOC_WORD"
                comment_init    = None
                comment_end     = None
                other_comment   = None
    else:
        print "\nINvalid extension"
        exit()
    properties =[dtype,comment_init,comment_end,other_comment]

    return properties

# remove all occurance streamed comments (/*COMMENT */) from line
def remove_double_comments(line,comment_init,comment_end):
    line = re.sub(re.compile("comment_init.*?comment_end",re.DOTALL ) ,"" ,line)
    return line

 # remove all occurance singleline comments (//COMMENT\n ) from line
def remove_single_comments(line,other_comment):
    line = re.sub(re.compile("other_comment.*?\n" ) ,"" ,line)
    return line

def compare(file1,file2):

    properties_file1 = identify(file1)
    properties_file2 = identify(file2)

    for line1, line2 in (file1, file2):
        line1 = line1[:-1]
        line2 = line2[:-1]

        #Manejar los disitintos tipos de comentarios segun tipo de archivo
        if properties_file1[0] != properties_file2[0]:
            print("DIFFERENT: Directly, file extensions do not agree")
        else:

            #ya he verificado que los archivos sean del mismo tipo,
            #entonces properties_file1 = properties_file2
            if properties_file1[1] != None and properties_file1[1] != None:

                if (line1.find(properties_file1[1]) != -1 and line1.find(properties_file1[2]) != -1):
                    remove_double_comments(line1,properties_file1[1],properties_file1[2])
                pass
                if (line2.find(properties_file1[1]) != -1 and line2.find(properties_file1[2]) != -1):
                    remove_double_comments(line2,properties_file1[1],properties_file1[2])
                pass
                if properties_file1[3] != None:
                    if (line1.find(properties_file1[3]) != -1):
                        remove_single_comments(line1,properties_file1[3])
                    pass
                    if (line2.find(properties_file1[3]) != -1):
                        remove_single_comments(line2,properties_file1[3])
                    pass
                pass
            elif properties_file1[3] != None:
                if (line1.find(properties_file1[3]) != -1):
                    remove_single_comments(line1,properties_file1[3])
                pass
                if (line2.find(properties_file1[3]) != -1):
                    remove_single_comments(line2,properties_file1[3])
                pass
            else:
                print"\nThere are no commetns to supress"
        pass

        if line1 == line2:
            outfile.write("The line is correct\n")
        else:
            outfile.write("Values do not agree --> " + line1 + "\n")
        pass


def usage():
    print "\nThis is..."


def main(argv):
    os.system("clear")

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:', ['help''input'])

    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-i', '--input'):
            file1 = sys.argv[2]
            file2 = sys.argv[3]
            compare(file1,file2)
            sys.exit(2)

#EJECUCION DEL main
if __name__ == '__main__':
    main(sys.argv[1:])
