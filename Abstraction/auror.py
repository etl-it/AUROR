#PROGRAMA PRINCIPAL

#Fuciones de Python
import sys, os, re, copy
import getopt
from ConfigParser import RawConfigParser

#Funciones propias
from menu import menu

#CARGAR FICHERO DE CONFIGURACION POR DEFECTO
default_cparser = RawConfigParser()
default_cparser.read('Auror_default.conf')


#Imprimir en pantalla el script y sus argumentos y opciones
print 'ARGV:', " ".join(sys.argv[0:]), "\n"

#Informacion de ayuda
def help():
    """Ayuda sobre opciones en linea de comandos """
    print "usage:",sys.argv[0], "[options]\n"
    print " -h this message\n"
    print " -i input file/s\n"
    print " -o output file\n"

def init_opt():
    #Definir los parametros obligatorios (:) y opcionales, en su forma abreviada y reducida
    try:
        options, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "input", "output"])
    except getopt.GetoptError as err:
        #Imprimir ayuda y salir si hay algun error o argumento incorrecto
        print str(err)
        help()
        sys.exit(2)
    output = None
    verbose = False

    #Definir el tipo de las variables que guardaran las opciones
    INP_input = ''
    INP_output = ''

    #Asignar las opciones a cada argumento
    for _opt, _arg in options:
        if _opt in ("-i", "--input"):
            INP_input = _arg
        elif _opt in ("-o", "--output"):
            INP_output = _arg
        elif _opt in ("-h", "--help"):
            help()
            sys.exit()
        else:
            assert False, "unhandled option"

    #Imprimir en pantalla todo lo anotado
    print "Argumentos y opciones: \n",
    for _opt,_arg in options :
        print " -"+_opt+": "+_arg

def main():
    #Clean the screen and show the menu once more
    os.system('clear')
    print("main")

    init_opt()

    while True:
        menu()
        #Ask for an option to the user
        optionMenu = input("Insert an option: >> ")

        if optionMenu == 1:
                print("Auror will operate in default mode. You dont have to configure any other parameter")
                break
        elif optionMenu == 2:
            print("You are gonna to personalize your own test")
            optionMenu2 = input("Please, select the configure parameters >>")




if __name__ == '__main__':
    main()
