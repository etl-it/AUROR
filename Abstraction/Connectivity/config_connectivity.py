import os
from ConfigParser import RawConfigParser

def select_hosts():
    host_tests = []

    end = False

    while end is False:

        host = raw_input('Insert hosts to verify if ping exits. When you dont wanna to configure more tests insert END. >>')

        host_tests.append(host)

        if host == "END":
            host_tests.remove(host)
            end = True

    return host_tests


def config_connectivity_conf(dir):

    current_dir = os.getcwd()
    config_connectivity_conf = "/usr/lab/alum/0330717/Auror_workspace/cc.conf"
    cparser = RawConfigParser()

    if current_dir != dir :
        os.chdir(dir)

    hosts_tests = select_hosts()

    with open(config_connectivity_conf, 'wb') as archivo:
        cparser.add_section("HOSTS")
        for host in hosts_tests :
            host_index = hosts_tests.index(host)
            host_name = 'HOST' + str(host_index)
            cparser.set("HOSTS", host_name, host)
        cparser.write(archivo)

def main():
    dir = "/usr/lab/alum/0330717/Auror_workspace"
    config_connectivity_conf(dir)

if __name__ == '__main__':
    main()
