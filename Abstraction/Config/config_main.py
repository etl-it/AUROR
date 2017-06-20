import os
from ConfigParser import RawConfigParser

def config_ini():

    dir = "/usr/lab/alum/0330717/Auror_workspace"


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
