#PROGRAMA PRINCIPAL

#Fuciones de Python
import sys, os, re, copy
import getopt
import subprocess

from ConfigParser import RawConfigParser
from os import path


#Funciones propias
from catcher import *
from functions import *


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

    output_file = "no_report.txt"
    report = False
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

                    # #HAN SELECCIONADO QUE QUIEREN UN REPORTE, LUEGO CREAMOS EL FICHERO
                    # index = 1
                    # output_file = "Auror" + str(index) + ".txt"
                    # if path.exists(output_file) is True:
                    #     new_index = index + 1
                    #     output_file = "Auror" + str(new_index)
                    report = True

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
                    elif int(test) == 3:
                        cparser.set('TESTS', 'Test3', 'Devices')

                cparser.write(archivo) #Se escribe el archivo de configuracion
        else:
            exit() #Finalizo la aplicacion si el usuario no quiere configurar nada
    #return output_file
    return report


def available_tests():
    print """
        1 => Connectivity
        2 => Architecture
        3 => Devices
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

def configurate_report(report_file, test_to_do):
    cparser = RawConfigParser()
    with open(report_file, 'wb') as archivo:
        for test in test_to_do:
            test_index = test_to_do.index(test)
            test_name = 'TEST' + str(test_index)
            cparser.add_section(test_name)
            cparser.set(test_name, test, "undone yet")
        cparser.write(archivo)


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
            report_file = _arg
        elif _opt in ("-h", "--help"):
            help()
            sys.exit()
        else:
            assert False, "unhandled option"

    #Imprimir en pantalla todo lo anotado
    print "Argumentos y opciones: \n",
    for _opt,_arg in options :
        print " -"+_opt+": "+_arg
    return [config_file,report_file]

def sort(test):
    type = ""

    possible_mix_tests = ["Connectivity"]
    possible_hardware_tests = ["Devices", "hola", "adios"]
    possible_software_tests = ["Architecture", "venga", "funciona"]

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
        if test == possible_software_tests[k_index]:
            type = "SOFTWARE"
        else:
            pass
    return type

def main():
    #Clean the screen and show the menu once more
    os.system('clear')


    test_to_do = []
    done_tests = []
    report = False
    usados = []

    #Mostramos por pantalla el modo de uso al usuario
    usage()

    #Seleccionar la opcion inicial del usaurio (help, fichero de cnfiguracion, o fichero de salida)
    #En el caso de que la opcion sea -i se guardara el fichero de configuracion inicial especificado
    files = init_opt()

    config_file = files[0]
    report_file = files[1]

    #Caracterizacion del fichero de configuracion a gusto del usuario
    #report_file = config(config_file)
    report = config(config_file)

    test_to_do = select_tests(config_file,test_to_do)

    configurate_report(report_file, test_to_do)

    # if report_file != "no_report.txt": #en este caso el usuario ha seleccionado la opcion de crear REPORTE
    #     configurate_report(report_file, test_to_do)
    #     report = True
    #     print("tests  en el fichero de salida")


    #CREACION DE LOS "CATCHER". Por defecto crearemos 3, uno de cada tipo
    catchers = []
    mix_catcher = MixCatcherFactory()
    catchers.append(mix_catcher)
    software_catcher = SoftwareCatcherFactory()
    catchers.append(software_catcher)
    hardaware_catcher = HardwareCatcherFactory()
    catchers.append(hardaware_catcher)
    aurors = []

    print test_to_do

    for test_name in test_to_do:
        if sort(test_name) == "MIX":
            id1 = random.randint(0,1000)
            auror_mix = mix_catcher.getMixCatcher(test_name,id1)
            aurors.append(auror_mix)
            print("creo mix")
            print(test_name)
            print(sort(test_name))
        if sort(test_name) == "SOFTWARE":
            id2 = random.randint(0,1000)
            auror_soft = software_catcher.getSoftwareCatcher("Architecture", id2)
            aurors.append(auror_soft)
            print("creo soft")
            print(test_name)
            print(sort(test_name))
        if sort(test_name) == "HARDWARE":
            id3 = random.randint(0,1000)
            auror_hard = hardaware_catcher.getHardwareCatcher("Devices", id3)
            aurors.append(auror_hard)
            print("creo hard")
            print(test_name)
            print(sort(test_name))
        else:
            pass

    print aurors
    for this_auror in aurors:

        if report is True:
            this_auror.catch_with_report(report_file, id)
        else:
            this_auror.catch()

if __name__ == '__main__':
    main()
