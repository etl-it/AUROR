import subprocess
import shlex


class Devices(Test):

    def __init__(self, id, description, type, catch_lspci):

        Devices.__init__(self, id , description, "Hardware")
        self.catch_lspci = catch_lspci


    def catch_lspci():
        process = subprocess.Popen(shlex.split('lspci'), stdout = subprocess.PIPE)

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print output.strip()

        rc = process.poll()
        return rc
