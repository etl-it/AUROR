
import subprocess
import shlex

# from catcher import *

class Devices(HardwareCatcher):

    def __init__(self, id):
        HardwareCatcher.__init__(self, "Hardware", id)

    def getId(self,HardwareCatcher):
        return HardwareCatcher.getId()

    def do_lspci(self, report_file, id):

        report_to_print = []

        if report_file != "no_report.txt":

            test_title = print_test_title(id)
            report_to_print.append(test_title)

            print """-----------------------------------"""
            st = """-----------------------------------"""
            report_to_print.append(st)

            process = subprocess.Popen(shlex.split('lspci'), stdout = subprocess.PIPE)

            # while True:
            #     output = process.stdout.readline()
            #     if output == '' and process.poll() is not None:
            #         break
            #     if output:
            #         print output.strip()

            rc = process.poll()
            print(rc)
            report_to_print.append(rc)

            with open(report_file, 'w') as fichero:
                for s in report_to_print:
                    fichero.write(s + '\n')
                fihcero.close()

    def do(self):
         process = subprocess.Popen(shlex.split('lspci'), stdout = subprocess.PIPE)

        # while True:
        #     output = process.stdout.readline()
        #     if output == '' and process.poll() is not None:
        #         break
        #     if output:
        #         print output.strip()

        #rc = process.poll()
        #return rc

    def catch(self):
        print(rc)


    def catch_with_report(self, report_file, id):
        self.do_lspci(report_file,id)
