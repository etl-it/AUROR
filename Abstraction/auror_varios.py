#PROGRAMA PRINCIPAL


#EMPIEZA POR ESTO : ====>>>>
#http://bioinfoperl.blogspot.com.es/2013/03/procesar-argumentos-multiples-opciones-python.html


#Fuciones de Python
from ConfigParser import RawConfigParser
import sys, os, re, copy

from types import *

#Funciones propias
import menu

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

def def_type_variables():
    #Definir el tipo de las variables que guardaran las opciones
    INP_input = []
    INP_output = ''
    #Asignar a cada argumento una de las anteriores variables
    options = {'h': 'help'} ###AQUI TE QUEDAS LORENA 

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
    print("main")
    init_opt()
    menu()

if __name__ == '__main__':
    main()
