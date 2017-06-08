
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
    auror_mix = mix_catcher.getMixCatcher("Connectivity")
    #auror_mix.catch(host_to_test)


    software_catcher = SoftwareCatcherFactory()
    auror_soft = software_catcher.getSoftwareCatcher("Architecture")
    #print(auror_soft.define_architecture())

    auror_soft.catch() 

if __name__ == '__main__':
    main()
