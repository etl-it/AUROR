import os
import subprocess

##class network(hardware,software):
##    pass

#-----------------------------------------------------------------------------
#Uso del comando de bash 'ping' para ver si existe conectividad
#lista de host (anadir lista de hosts).
#Enviamos 5 paquetes ('-c 5') y esperamos 3ms ('-w 3') la respuesta
#La funcion devuelve el codigo de salida del comando ping_output_code
def ping_output_code(hostname):

    output_code = subprocess.call(['ping', '-c', '5', '-w', '15', hostname],
                                    stdout = open(os.devnull,'w'),
                                    stderr = open(os.devnull,'w'))
    return output_code


#-----------------------------------------------------------------------------
#Para cada hostname de la lista, se verifica si hay ping
#Develve un objeto dict donde key = hostaname
#                             values = return code del ping
#Los host sona verificar son los de nuestro sistema ((??? DECALARAR COMO UNA ESPECIE DE CTES???))
def verify_host_list(host_list):

    return_output_codes = dict()

    for hostname in host_list:
        return_output_codes[hostname] = ping_output_code(hostname)

    return return_output_codes

def main():
    ##????VER SI DE ALGNA FORMA ESTO LO PUEDO SACAR FUERA
    host_to_test = [
        'google.com',
        '163.117.144.243', ##alcazar01.lab.it.uc3m.es
        '163.117.168.105'
    ]
    print verify_host_list(host_to_test)

if __name__ == '__main__':
    main()
