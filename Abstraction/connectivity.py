import os
import subprocess

from catcher import *

class Connectivity(MixCatcher):
    def __init__(self):
        MixCatcher.__init__(self, "Connectivity")


    def ping_output_code(self, hostname):

        output_code = subprocess.call(['ping', '-c', '5', '-w', '15', hostname],
        stdout = open(os.devnull,'w'),
        stderr = open(os.devnull,'w'))
        return output_code

    def verify_host_list(self, host_list):

        return_output_codes = dict()

        for hostname in host_list:
            return_output_codes[hostname] = self.ping_output_code(hostname)
            print hostname
            print """\t"""
            if return_output_codes[hostname] == 0:
                print("OK")
                print """\t"""
            else:
                print("ERROR")
                print """\t"""


    def catch(self,params): #params = host_list
        verify_host_list(params)

def main():
    #Clean the screen and show the menu once more
    #os.system('clear')
    print("main")

    host_to_test = ['google.com',
                    '163.117.144.243', ##alcazar01.lab.it.uc3m.es
                    '163.117.168.105'
                    ]

    mix_catcher = MixCatcherFactory()
    auror = mix_catcher.getMixCatcher("Connectivity")
    #auror.catch(host_to_test)
    auror.verify_host_list(host_to_test)



if __name__ == '__main__':
    main()
