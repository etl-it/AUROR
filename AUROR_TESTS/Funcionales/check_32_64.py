#Script to check if a system has an 64 or 32 architecture. By default it will be a 32-bit-architecture

import os
import subprocess

def define_architecture():
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

def main():

    print define_architecture()

if __name__ == '__main__':
    main()
