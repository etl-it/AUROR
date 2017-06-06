
#import connectivity
from catcher import *
import os
import subprocess


def main():
    #Clean the screen and show the menu once more
    os.system('clear')
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
