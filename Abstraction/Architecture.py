from catcher import *
from functions import *


class Architecture(SoftwareCatcher):
    #"CONSTRUCTOR"
    def __init__(self, id):
        SoftwareCatcher.__init__(self, "Architecture",id)

    def getId(self, SoftwareCatcher):
        return SoftwareCatcher.getId()

    #Metodo Propio
    def define_architecture(self):
        process = subprocess.Popen(['uname', '-m'], stdout = subprocess.PIPE)

        out_value = process.communicate()[0]

        out_value = out_value [:-1]

        if out_value == 'x86_64':
            type = 1 #64 bytes
        else:
            type = 0

        info = [type, out_value]

        return info

    #Metodo para generalizacion con factoria
    def catch(self,id):
        try:
            print(print_test_title(id))
            print(self.define_architecture())
        except:
            print """ERROR"""
            sys.exit(2)

    def catch_with_report(self,report_file, id):

        report_to_print = []

        if report_file != "no_report.txt":

            print('\n' + print_test_title(id) + '\n')
            print(test_title)
            report_to_print.append(test_title)


            s = self.define_architecture()
            report_to_print.append(s)

            with open(report_file, 'w') as fichero:
                for s in report_to_print:
                    fichero.write(s + '\n')
                    fichero.close()
            print("Ejecuto test arch")
