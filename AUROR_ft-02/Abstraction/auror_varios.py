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

def init_opt():
    #Definir el tipo de las variables que guardaran las opciones
    INP_input = []
    INP_output = ''
    #Asignar a cada argumento una de las anteriores variables
    options = {'h': 'help', 'help': 'help', 'i': 'INP_input', 'input': 'INP_input', 'o': 'INP_output', 'output': 'INP_output'}
    arg_var = str()
    #Leer los argumentos y opciones
    for _argv in sys.argv[1:] :
      # Leer los argumentos que comienzan con guion
      if re.match("^-", _argv) :
           for _opt,_var in options.iteritems() :
                if re.compile("^-%s$" % (_opt)).match(_argv) :
                     argv_var = copy.deepcopy(_var)
                     if type(vars()[argv_var]) is FunctionType :
                          vars()[argv_var]()
                     break
      # Anotar las opciones de cada argumento
      else :
           if argv_var is not None :
                if type(vars()[argv_var]) is ListType :
                     vars()[argv_var].append(_argv)
                else:
                     vars()[argv_var] += _argv
     # Imprimir en pantalla todo lo anotado
     print "Script:",sys.argv[0],"\n"
     print "Argumentos y opciones:\n",
     for _opt,_var in options.iteritems() :
          if vars()[_var] is not None and type(vars()[_var]) is not FunctionType:
               #print _opt,pprint(type(vars()[_var]))
               if type(vars()[_var]) is ListType:
                    print " -"+_opt+": "+str(", ".join(vars()[_var]))
               else :
                    print " -"+_opt+": "+str(vars()[_var])


def main():
    print("main")
    init_opt()
    menu()

if __name__ == '__main__':
    main()
