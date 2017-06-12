
import subprocess
import shlex

from AurorTest import AurorTest

class Devices(HardwareCatcher):

    def __init__(self, id):
        HardwareCatcher.__init__(self, "Hardware", id)

    def getId(self. HardwareCatcher):
        return HardwareCatcher.getId()

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

    def catch(self):
        print(self.catch_lspci())

    def catch_with_report(self, report, file):
    
