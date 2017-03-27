import MySQLdb

##Para conectarnos a la base de datos y ejecutar cualquier consulta:
##1 -> Abrir la conexión y crear un puntero
##2 -> Ejecutar la consulta
##3 -> Traer los resultados si se trata de un selección, o hacer efectiva la
##     cuando se actualiza o se eliminan datos
##4 -> Cerrar el puntero y la conexión

##ACCEDER BASE DE DATOS

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'mysqlroot'
DB_NAME = 'a'

def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*datos) #Conectar a la base de datos
    cursor = conn.cursor() #Crear un cursor
    cursor.execute(query) #Ejecutar una consulta

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall() # Traer los resultados de un SELECT
    else:
        conn.commit() #Hacer efectiva la escritura de datos
        data = None

    cursor.close() # Cerrar el cursor
    conn.close()   # Cerrar la conexión

    return data

##INSERTAR DATOS

daro = raw_input("Dato: ")
query = "INSERT INTO b (b2) VALUES ('%s')" % dato
run_query(query)

##SELECCIONAR TODOS LOS REGISTROS

query = "SELECT b1, b2 FROM b ORDER BY b2 DESC"
result = run_query(query)
print result

##SELECCIONAR SÓLO REGISTROS COINCIDENTES

criterio = raw_input("Ingrese criterio de bśqueda: ")
query = "SELECT b1, b2 FROM b WHERE b2 = '%s'" % criterio
result = run_query(query)
print result

##ELIMINAR REGISTROS

criterio = raw_input("Ingrese criterio p7 eliminar coincidencias: ")
query = "DELETE FROM b WHERE b2 = '%s'" % criterio
run_query(query)

##ACTUALIZAR DATOS

b1 = raw_input("ID: ")
b2 = raw_input("NUevi valor: ")
query = "UPDATE b SET b2='%s'" WHERE b1 = %i" % (b2, int(b1))
