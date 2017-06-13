#import connectivity
from catcher import *
import os
import subprocess


def main():
    #Clean the screen and show the menu once more
    os.system('clear')
    print("main")

    report_file = "hola.txt"

    host_to_test = ['google.com',
                    '163.117.144.243', ##alcazar01.lab.it.uc3m.es
                    '163.117.168.105'
                    ]

    mix_catcher = MixCatcherFactory()
    auror_mix = mix_catcher.getMixCatcher("Connectivity", 2)
    #auror_mix.catch(host_to_test)


    software_catcher = SoftwareCatcherFactory()
    auror_soft = software_catcher.getSoftwareCatcher("Architecture", 3)
    print(auror_soft.catch_with_report(report_file, 4))

    hardaware_catcher = HardwareCatcherFactory()
    auror_hard = hardaware_catcher.getHardwareCatcher("Devices", 4)
    auror_hard.catch_with_report(report_file, 4)

    #auror_soft.catch()

if __name__ == '__main__':
    main()
