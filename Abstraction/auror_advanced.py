#PROGRAMA PRINCIPAL

#Fuciones de Python
import sys, os, re, copy
import getopt
import subprocess

from ConfigParser import RawConfigParser
from os import path


#Funciones propias
from catcher import *


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
          por defecto seleccionar [auror_default.conf]\n
    [-o]                  => Fichero de salida\n
    [-h]                  => AYUDA
    """

def configuration_file_style():
    print("AUROR CONFIGURATION FILE STYLE")
    print """
        [BASIC]
        SeverityLevel = 'l/m/h' [LOW/MEDIUM/HIGH]
        Report = 'y/n' [YES/NO]

        [TESTS]
        Test1 = ...
        Test2 = ...
        Test3 = ...
        .
        .
        .

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
        print('La aplicacion aun no se ha configurado correctamente')
        continuar = raw_input('Desea configurarla ahora? (y/n) ')
        #Creo el archivo de configuracion
        if continuar.lower() == 'y' :
            cparser = RawConfigParser() #Se crea el objeto ConfigParser
            with open(config_file, 'wb') as archivo:
                configuration_file_style() #Se muestra al usario la fomra que debe tener el fihchero de configuracion

                cparser.add_section('BASIC')
                cparser.add_section('TESTS')

                severity = raw_input('Seleccione el grado de profundidad de los tests: >> ')
                if severity.lower() == 'l':
                    cparser.set('BASIC', 'SeverityLevel', 'LOW')
                elif severity.lower() == 'm':
                    cparser.set('BASIC', 'SeverityLevel', 'MEDIUM')
                elif severity.lower() == 'h':
                    cparser.set('BASIC', 'SeverityLevel', 'HIGH')

                report = raw_input("Desea guardar un informe? >> ")
                if report.lower() == 'y':
                    cparser.set('BASIC', 'Report', 'YES')
                elif report.lower() == 'n':
                    cparser.set('BASIC', 'Report', 'NO')

                number_of_tests = raw_input('Introduzca el numero de test que quiere llevar a cabo: >> ')

                range_number_of_tests = range(int(number_of_tests))

                for test in range_number_of_tests:
                    available_tests()

                    test = raw_input('Introduzca el identificador del test que quiere realizar: >>')
                    if int(test) == 1:
                        cparser.set('TESTS', 'Test1', 'Connectivity')
                    elif int(test) == 2:
                        cparser.set('TESTS', 'Test2', 'Architecture')

                cparser.write(archivo) #Se escribe el archivo de configuracion
        else:
            exit() #Finalizo la aplicacion si el usuario no quiere configurar nada


def available_tests():
    print """
        1 => Connectivity
        2 => Architecture
        3 =>
        .
        .
        .
    """

def select_tests(config_file,test_to_do):
    cparser = RawConfigParser()
    cparser.read(config_file)

    #all_tests = cparser.options('TESTS')

    options_tests = cparser.options('TESTS')

    all_tests = [] #Lista con los NOMBRES de los tests seleccionados por el usuario

    for option_test in options_tests:
        #option_index = options_tests.index(option_test)
        all_tests.append(cparser.get('TESTS',option_test))

    for test in all_tests:
        test_to_do.append(test)

    return test_to_do

def move_to_done(test,test_to_do,done_tests):
    test_to_do.remove(test)
    done_tests.append(test)

#def report:

def init_opt():
    config_file = ' ' #Fihero de config por defecto
    #Definir los parametros obligatorios (:) y opcionales, en su forma abreviada y reducida
    try:
        options, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "input", "output"])
        #Imprimir ayuda y salir si hay algun error o argumento incorrecto
    except getopt.GetoptError as err:
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
    return config_file

def sort(test):
    type = ""

    possible_mix_tests = ["Connectivity"]
    possible_hardware_tests = ["Este"]
    possible_software_tests = ["Architecture"]

    for i in possible_mix_tests:
        i_index = possible_mix_tests.index(i)
        if test == possible_mix_tests[i_index]:
            type = "MIX"
        else:
            pass
    for j in possible_hardware_tests:
        j_index = possible_hardware_tests.index(j)
        if test == possible_hardware_tests[j_index]:
            type = "HARDWARE"
        else:
            pass
    for k in possible_software_tests:
        k_index = possible_software_tests.index(k)
        if test == possible_hardware_tests[k_index]:
            type = "SOFTWARE"
        else:
            pass
    return type

def main():
    #Clean the screen and show the menu once more
    os.system('clear')


    test_to_do = []
    done_tests = []

    #Mostramos por pantalla el modo de uso al usuario
    usage()

    #Seleccionar la opcion inicial del usaurio (help, fichero de cnfiguracion, o fichero de salida)
    #En el caso de que la opcion sea -i se guardara el fichero de configuracion inicial especificado
    config_file = init_opt()

    #Caracterizacio del fichero de configuracion a gusto del usuario
    config(config_file)

    test_to_do = select_tests(config_file,test_to_do)

    #CREACION DE LOS "CATCHER". Por defecto crearemos 3, uno de cada tipo
    mix_catcher = MixCatcherFactory()
    software_catcher = SoftwareCatcherFactory()
    hardaware_catcher = HardwareCatcherFactory()

    aurors = []

    for test_name in test_to_do:
        print(sort(test_name))
        if sort(test_name) == "MIX":
            auror_mix = mix_catcher.getMixCatcher(test_name)
            aurors.append(auror_mix)
        elif sort(test_name) == "SOFTWARE":
            auror_soft = software_catcher.getSoftwareCatcher(test_name)
            aurors.append(auror_soft)
        elif sort(test_name) == "HARDAWARE":
            auror_hard = hardaware_catcher.getHardwareCatcher(test_name)
            aurors.append(auror_hard)
        else:
            print("No hay tests para crear aurores")

    for this_auror in aurors:
        this_auror.catch()


if __name__ == '__main__':
    main()
