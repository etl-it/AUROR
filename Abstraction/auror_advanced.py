#PROGRAMA PRINCIPAL

#Fuciones de Python
import sys, os, re, copy
import getopt
#from ConfigParser import RawConfigParser
import configparser
from ConfigParser import RawConfigParser
from os import path


#Funciones propias
from menu import menu
from menu import possible_tests
from connectivity import Connectivity
from AurorTest import AurorTest
from architecture import Architecture
from devices import Devices


test_to_do = []

#CARGAR FICHERO DE CONFIGURACION POR DEFECTO
#default_cparser = RawConfigParser()

#Imprimir en pantalla el script y sus argumentos y opciones
print 'ARGV:', " ".join(sys.argv[0:]), "\n"

def usage():
    print("AUROR AUDIT SYSTEM")
    print """
    \t \t \t pyhton auror.py [-i] [-o] [-h]\n
    [-i] [my_auror.conf] => Seleccionar un fichero de configuracion
                            si queremos uno distinto al que existe
                            por defecto

                            Debera tener la forma : [nombreQueDesee.conf]

          Si queremos cargar el fichero de configuracion
          por defecto seleccionar [auror_default.conf]
    [-o]                  => Fichero de salida
    [-h]                  => AYUDA
    """

def configuration_file_style():
    print("AUROR CONFIGURATION FILE STYLE")
    print """
    """

#Informacion de ayuda
def help():
    """Ayuda sobre opciones en linea de comandos """
    print "usage:",sys.argv[0], "[options]\n"
    print " -h this message\n"
    print " -i input file/s\n"
    print " -o output file\n"

def config(config_file):
    #Si el archivo de configuracion no existe
    if path.exists(config_file) is False:
        #Pregunto si lo quiere crear
        print('La aplicación aún no se ha configurado correctamente')
        continuar = raw_input('¿Desea configurarla ahora? (y/n) ')
        #Creo el archivo de configuracion
        if continuar.lower() == 'y' :
            cparser = RawConfigParser() #Se crea el objeto ConfigParser
            with open(config_file, 'wb') as archivo:
                configuration_file_style() #Se muestra al usario la fomra que debe tener el fihchero de configuracion
                cparser.write(archivo) #Se escribe el archivo de configuracion
        else:
            exit() #Finalizo la aplicacion si el usuario no quiere configurar nada



def select_tests(config_file):
    cparser = RawConfigParser()
    cparser.read(config_file)
    for key in cparser['test_to_do']:
        test_to_do.append(key)

def move_to_done(test):

def report:

def init_opt():

    config_file = 'Auror_default.conf' #Fihero de config por defecto

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
            config_file = _arg
            config(config_file)
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
    usage()

    init_opt()

    while True:
        menu()
        #Ask for an option to the user
        optionMenu = input("Insert an option: >> ")

        if optionMenu == 1:
                print("Auror will operate in default mode. You dont have to configure any other parameter")
                break
        elif optionMenu == 2:
            print("BASIC MODE")
            possible_tests()
            optionMenu2 = input("Please, select the configure parameters >>")

            if optionMenu2 == 0:
                myAuror = Connectivity(1,"ping","MIX")

                host_to_test = ['google.com',
                                '163.117.144.243', ##alcazar01.lab.it.uc3m.es
                                '163.117.168.105'
                                ]
                print """\n"""
                print myAuror.verify_host_list(host_to_test)
                myAuror.verify_host_list(host_to_test)
                print """\n"""
            elif optionMenu2 == 1:
                myAuror2 = Architecture(2, "Arquitectura", "SOFTWARE")
                print """\n"""
                print myAuror2.define_architecture()
                print """\n"""
            elif optionMenu2 == 3:
                myAuror3 = Devices(3, "LSPCI", "HARDWARE")
                print """\n"""
                myAuror3.catch_lspci()
                print """\n"""
            else:
                sys.exit()

if __name__ == '__main__':
    main()
