import os


def menu():

    print('Select an option:')
    print("\t1 - DEFAULT")
    print("\t2 - BASIC MODE : Un unico test a la vez")
    print("\t3 - ADVANCED MODE : Ejecuta varios tests a la vez tras la previa selecceccion de una lista de tests disponibles")
    print("\t4 - Goodbye AUROR")

def possible_tests():
    print """
    \t [0] => Check if it's possible a connection to your hosts with ping
    \t [1] => Check if your system has an 64 or 32 architecture
    \t [2] => LSPCI

    """
