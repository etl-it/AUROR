
from time import sleep

#Variables globales para definir los estados
state_inic = 'i'
state_config = 'c'
state_basic_test = 'bc'
state_my_test = 'mt'
state_report = 'r'

def INICIO(start,config):
    global current_state
    print('Initial State')
    #Transiciones
    sleep(2)
    if start == 0:
        current_state = 'i'
    if start == 1 and config == 1:
        current_state = 'c'
        print('Trasition to Config State')
    if start == 1 and config == 0:
        current_state = 'bt'
        print('Trasition Basic test')
        
def CONFIG(start,config_done):
    global current_state
    print('Config State')
    #Transiciones
    sleep(2)
    if config_done == 1:
        current_state = 'mt'
        print('Transition to My Test')
    if start == 1:
        current_state = 's'
        print('Back to Start')


def BASIC_TEST(start,test_done):
    global state
    print('Basic Test State')
    #Transiciones
    sleep(2)
    if test_done == 1:
        current_state = 'r'
        print('Transition to Report')
    if start == 1:
        current_state = 's'
        print('Back to Start')


def MY_TEST(start,test_done):
    global state
    print('My Test State')
    #Transiciones
    sleep(2)
    if test_done == 1:
        current_state = 'r'
        print('Transition to Report')
    if start == 1:
        current_state = 's'
        print('Back to Start')

def REPORT(start,report_done):
    global state
    print('Report State')
    if start == 1 or report_done == 1:
        current_state = 's'
        print('Back to Start')
