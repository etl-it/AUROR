
class Devices(HardwareCatcher):

    def __init__(self, id):
        HardwareCatcher.__init__(self, "Hardware", id)

    def getId(self, HardwareCatcher):
        return HardwareCatcher.getId()

    def do_lspci(self, report_file, id):

        report_to_print = []

        if report_file != "no_report.txt":

            salt = '\n'
            test_title = print_test_title(id)
            report_to_print.append(salt)
            report_to_print.append(test_title)

            print('\n')
            print(test_title)
            print """**************************************"""

            st_pre = """**************************************""" +'\n'
            st = """-----------------------------------"""
            report_to_print.append(st_pre)
            report_to_print.append(st)

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

            with open(report_file, 'a') as fichero:
                for s in report_to_print:
                    if s != None:
                        s = str(s)
                        fichero.write(s + '\n')
                fichero.close()

    def do(self):
        process = subprocess.Popen(shlex.split('lspci'), stdout = subprocess.PIPE)

        # for i in range(1,10):
        #     output = process.stdout.readline()
        #     if output == '' and process.poll() is not None:
        #         break
        #     if output:
        #         print output.strip()

        rc = hola
        return rc

    def catch(self):
        rc = "hola"
        print(rc)


    def catch_with_report(self,report_file, id):
        self.do_lspci(report_file,id)
