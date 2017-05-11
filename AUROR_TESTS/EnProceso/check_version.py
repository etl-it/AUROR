import os
import subprocess
import shlex


def check_version_package(package):
    process = subprocess.call(['dpkg', '--list', package]),stdout = open(os.devnull,'w'))


    while True:
        output = process.stdout.readLine()
        print output.strip()

        rc = process.poll()
        print rc
        return rc



def main():

    print check_version_package('apache2')


if __name__ == '__main__':
    main()
