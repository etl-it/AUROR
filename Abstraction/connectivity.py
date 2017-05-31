import os
import subprocess

class Connectivity(AurorTest):

    def __init__ (self, id, description, type, ping_output_code, verify_host_list):
        Connectivity.__init__(self, id, description, "Mix")
        self.ping_output_code = ping_output_code
        self.verify_host_list = verify_host_list

    def ping_output_code(hostname):

        output_code = subprocess.call(['ping', '-c', '5', '-w', '15', hostname],
                                        stdout = open(os.devnull,'w'),
                                        stderr = open(os.devnull,'w'))
        return output_code

    def verify_host_list(host_list):

        return_output_codes = dict()

        for hostname in host_list:
            return_output_codes[hostname] = ping_output_code(hostname)

        return return_output_codes
