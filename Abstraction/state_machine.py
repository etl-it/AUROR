
from time import sleep

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
        state =

def CONFIG(start,config):

def BASIC_TEST():

def MY_TEST():

def REPORT():
