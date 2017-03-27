##ConfigParser hereda de RawConfigParser; SafeConfigParser hereda a su vez se ConfigParser

from ConfigParser import ConfigParser

config = ConfigParser() #instancia de la clase ConfigParser
config.read("tema.cfg") #le indicamos el archivo sobre el que vamos a trabajar

sections = config.sections()
print("%d secciones:" % len(sections)) #cantidad de secciones

#Imprimir cada sección
for section in config.sections():
    print(section)

#Leer la cantidad de temas contenidos en el archivo
themes_count = config.get("GENERAL", "temas") ##get(nombre_seccion,ítem)

#Al tratarse de un archivo de texto, el valor de retorno es una cadena, lo convertimos
themes_count = config.getint("GENERAL","temas")
print(themes_count, type(themes_count)) #comprobamos que sea un entero

#Recibir una sección y devolver los ítems con sus respectivos valores
for item in config.items("TEMA"):
    print(item[0],item[1]) ##tupla con nombre_item + valor

#Imprimir todos los valores de todas las secciones del archivo
for section in config.sections():
    print("\n[%s]" % section)
    for item in config.items(section):
        print(item[0], ":", item[1])

#Alterar el valor de cualquier ítems
config.set("GENERAL", "temas", themes_count + 1)
config.set("TEMA", "nombre", "Tema Claro")
config.set("TEMA", "version", 1.2)
config.set("TEMA", "autor", "Desconocido")
config.set("TEMA", "votos", 51)

#Crear una nueva sección
config.add_section("TEMA3")
config.set("TEMA3", "nombre", "Tema Nuevo")
config.set("TEMA3", "version", 0.1)
config.set("TEMA3", "autor", "Python")
config.set("TEMA3", "votos",1)

##eliminar una sección
config.remove_section("TEMA3")

#eliminar un ítem
config.remove_option("TEMA3", "votos")

#guardar los cambios con write
with open("tem.cfg", "w") as f:
    config.write(f)
