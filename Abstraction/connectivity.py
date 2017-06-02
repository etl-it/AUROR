import os
import subprocess

from AurorTest import AurorTest

class Connectivity(AurorTest):

    def __init__ (self, id, description, type):
        AurorTest.__init__(self, id, description)
        self.__type = type


    def ping_output_code(self, hostname):

        output_code = subprocess.call(['ping', '-c', '5', '-w', '15', hostname],
        stdout = open(os.devnull,'w'),
        stderr = open(os.devnull,'w'))
        return output_code

    def verify_host_list(self, host_list):

        return_output_codes = dict()

        for hostname in host_list:
            return_output_codes[hostname] = self.ping_output_code(hostname)

        return return_output_codes
