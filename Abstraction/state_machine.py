
from time import sleep


@http://stg-pepper.blogspot.com.es/2016/04/maquina-de-estados-finitos-en-python.html
@http://www.w3ii.com/es/automata_theory/moore_and_mealy_machines.html
@http://recursospython.com/guias-y-manuales/multiprocessing-tareas-concurrentes-con-procesos/

#Variables globales para definir los estados
state_inic = 'i'
state_config = 'c'
state_basic_test = 'bc'
state_my_test = 'mt'
state_report = 'r'

def INICIO(start,config):
    global state
    print('Initial State')
    #Transiciones
    sleep(2)
    if start == 0:
        state = 'i'
    if start == 1 and config == 1:
        state = 'c' #Pasamos al estado de configuración
        print('Trasition to Config State') #Aquí habrá que pedir de algún modo los params de config
                                            #o procesar si es que ya nos los han metido;
                                            #he de ver cuál es la forma más óptima de realizar esto
    if start == 1 and config == 0:
        state = 'dt' #Pasamos al estado de test por defecto (test basico)
        print('Trasition Basic test') #Aquí no va a tener que haber nigún manejo de parmas
                                      #ya que esté test estará precargado por defecto



######PROBLEMA: donde especifico que la configuracion se ha terminado????
######----->>> MANEJAR LAS SALIDAS PARA QUE INFLUYAN EN LOS ESTADOS
##OPCION UNO: Puedo pasar otras entradas con las que pueda calcular si ha termiando o no
##OPCION DOS: Pasar directamente la salida aunque no acabo de verle todo el sentido

def CONFIG(start): #aquí ya voy a tener que manejar una salida
    global state

    #variable para indicar si se ha terminado el proceso de configuración de nuestro test
    config_done = 0

    print('Config State')
    #Transiciones
    sleep(2)

def BASIC_TEST(start):
    global state
    print('Basic Test State')

def MY_TEST(start):
    global state
    print('My Test State')

def REPORT(start):
    global state
    print('Report State')
