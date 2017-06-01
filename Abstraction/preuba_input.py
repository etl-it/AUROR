#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
     Script que usa el módulo 'getopt' para parsear los argumentos y opciones de línea de comandos
"""
import sys, re, os, copy
# Importar el módulo 'getopt'
import getopt
# Imprimir en pantalla el script y sus argumentos y opciones
print 'ARGV:', " ".join(sys.argv[0:]),"\n"
# Información de ayuda de uso del script
def help() :
     """Ayuda sobre opciones del script en línea de comandos"""
     print "usage:",sys.argv[0], "[options]\n"
     print " -h this message\n"
     print " -i input file/s\n"
     print " -o output file\n"
# Definir los argumentos obligatorios (:) y opcionales, en sus formas abreviada y completa
try:
     options, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "input", "output"])
except getopt.GetoptError as err:
     # Imprimir ayuda y salir si hay algún error o argumento incorrecto
     print str(err)
     help()
     sys.exit(2)
output = None
verbose = False
# Definir el tipo de las variables que guardarán las opciones
INP_input = ''
INP_output = ''
# Asignar las opciones a cada argumento
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
# Imprimir en pantalla todo lo anotado
print "Argumentos y opciones:\n",
for _opt,_arg in options :
     print " -"+_opt+": "+_arg
