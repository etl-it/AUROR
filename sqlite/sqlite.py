#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

#Si la base de datos no existe, se creeará con la ruta especificada
connection = sqlite3.connect('/tmp/prueba.db') #conexión con el objeto que representa la base de datos

#Si lo que queremos es que nuestra base de datos se vargue sóo en memoria...
#connection =sqlite3.connect(':memory:')

cursor = connection.cursor() #objeto cursor (obtener/instertar/acutalizar/borrar datos de nuestra base de datos)

print u"La base de datos se abrió correctamente"

#create a table
cursor.execute('''CREATE TABLE stocks
                    (date text, trans text, symbol text, qty real, price real)''')

#insert a row of data
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

#save the changes
connection.commit()

#close the connection
connection.close()
