from ConfigParser import RawConfigParser
from os import path



#Si el archivo de configuración no exite (habria que ver en que opcion se esta; ficheor_cfg por defecto siempre;
#luego ver si cargar el por defecto o nuevo fichero; ver si manejar en menu)

#Si el archivo de configuaracion no existe
if path.exists('my_auror.conf') is False:
    #Pregunto si lo quiere crear
    print('La aplicación aún no se ha configurado correctamente')
    continuar = raw_input('¿Desea configurarla ahora? (y/n) ')
    #Creo el archivo de configuaracion
    if continuar.lower() == 'y' :
        cparser = RawConfigParser() #Se crea el objeto ConfigParser
        with open('my_auror.conf', 'wb' ) as archivo:
            cparser.write(archivo) #Se escribe el archivo de configuracion
    else:
        exit() #Finzalizo la aplicacion si el usuario eligio no configurar nada

print('Auror begin testing')

def main():
    print("main")

if __name__ == '__main__':
    main()
