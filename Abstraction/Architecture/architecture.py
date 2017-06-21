import sys, os, subprocess
from Catcher import catcher
from Catcher.functions import format1, format2

class Architecture(catcher.SoftwareCatcher):
    #"CONSTRUCTOR"
    def __init__(self, id):
        catcher.SoftwareCatcher.__init__(self, "Architecture",id)

    def getId(self, MixCatcher):
        return cathcer.SoftwareCatcher.getId()

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


    def catch(self,report_file, id):

        report_to_print = []

        format1(id,report_to_print)


        s = self.define_architecture()
        print(s)
        report_to_print.append(s)

        if report_file != "no_report.txt":

            with open(report_file, 'a') as fichero:
                for s in report_to_print:
                    if s != None:
                        s = str(s)
                        fichero.write(s + '\n')
                fichero.close()
