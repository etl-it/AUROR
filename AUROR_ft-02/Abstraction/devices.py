import subprocess
import shlex

from AurorTest import AurorTest

class Devices(AurorTest):

    def __init__(self, id, description, type):

        AurorTest.__init__(self, id , description)
        self.__type = type


    def catch_lspci(self):
        process = subprocess.Popen(shlex.split('lspci'), stdout = subprocess.PIPE)

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print output.strip()

        rc = process.poll()
        return rc
