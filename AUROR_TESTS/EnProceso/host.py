
from argparse import ArgumentParser
import subprocess
import os
import sys



class Host(object):

    client = None

    #my_hosts = []
    #my_clients = []

    #Constructor por defecto
    def __init__(self, host = 'hostname', username = None, password = None):
        self.host = host
        self.username = username
        self.password = password

        #Si se nos han conectado remotamente
        if self.is_remote():
            self.client = get_ssh_client(self.host, self.username, self.password)
            #self.add_host(client)

    def is_remote():
        return self.host != 'localhost'

    def __del__(self):
        if self.client:
        self.client.close()

    #def add_host(client):
    #    self.my_hosts.append(client)

    #def connect():
    #    for host in self.host:


    def exec_command(self,cmd):
        if self.is_remote():
            return remote_command(self.client, cmd)
        else:
            return local_command(cmd)
