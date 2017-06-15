import os
from ConfigParser import RawConfigParser

#ver si el fichero de configuracion ya existe en el directorio

#dir = "/usr/lab/alum/0330717/Auror_workspace"


def select_hosts():
    host_tests = []

    end = False

    while end is False :

        host = raw_input("Insert hosts to verify if ping exits.\n When you dont wanna to configure more tests insert END. >>")

        host_tests.append(host)

        if hosts == "END":
            end = True

    return hosts_tests


def config_connectivity_conf(dir):

    current_dir = os.getCwd()
    config_connectivity_conf = "cc.conf"
    cparser = RawConfigParser()

    if current_dir != dir :
        os.chdir(dir)

    hosts_tests = select_hosts()

    with open(config_connectivity_conf, 'wb') as archivo:
        for host in hosts_tests :
            host_index = hosts_tests.index(tests)
            host_name = 'HOST' + str(host_index)
            cprser.set("HOSTS", host_name, host)
        cparser.write(archivo)

def main():
    dir = "/usr/lab/alum/0330717/Auror_workspace"
    config_connectivity_conf(dir)

if __name__ == '__main__':
    main()
