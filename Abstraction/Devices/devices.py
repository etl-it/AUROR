import sys, os, subprocess, shlex
from Catcher import catcher
from Catcher.functions import format1, format2

class Devices(catcher.HardwareCatcher):

    def __init__(self, id):
        catcher.HardwareCatcher.__init__(self, "Hardware", id)

    def getId(self, HardwareCatcher):
        return catcher.HardwareCatcher.getId()

    def do_lspci(self, report_file, id):

        report_to_print = []

        format1(id, report_to_print)

        process = subprocess.Popen(shlex.split('lspci'), stdout = subprocess.PIPE)

        for i in range(1,10):
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print output.strip()

        rc = process.poll()
        print(rc)
        report_to_print.append(rc)

        if report_file != "no_report.txt":

            with open(report_file, 'a') as fichero:
                for s in report_to_print:
                    if s != None:
                        s = str(s)
                        fichero.write(s + '\n')
                fichero.close()



    def catch(self,report_file, id):
        self.do_lspci(report_file,id)
