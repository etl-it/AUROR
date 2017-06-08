#Script to check if a system has an 64 or 32 architecture. By default it will be a 32-bit-architecture

import os
import subprocess
import sys

from catcher import *


class Architecture(SoftwareCather):
    #"CONSTRUCTOR"
    def __init__(self):
        SoftwareCather.__init__(self, "Software")

    #Metodo Propio
    def define_architecture(self):
        process = subprocess.Popen(['uname', '-m'],

                                    stdout = subprocess.PIPE,
                                    )
        out_value = process.communicate()[0]

        out_value = out_value [:-1]

        if out_value == 'x86_64':
            type = 1 #64 bytes
        else:
            type = 0

        info = [type, out_value]

        return info

    #Metodo para generalizacion con factoria
    def catch(self):

        info = self.define_architecture()
        print(info)


def main():
    software_catcher = SoftwareCatcherFactory()
    auror = software_catcher.getHardwareCatcher("Architecture")
    auror.catch()

if __name__ == 'main':
    main()
