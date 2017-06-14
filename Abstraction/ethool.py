class Ethtool(SoftwareCatcher):
    #"CONSTRUCTOR"
    def __init__(self, id):
        SoftwareCatcher.__init__(self, "Architecture",id)

    def getId(self, MixCatcher):
        return SoftwareCatcher.getId()

    def do_ethtool(self, report_file, id):

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

            process = subprocess.Popen(shlex.split(['sudo', 'ethtool', 'eth0']), stdout = subprocess.PIPE)

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

    def catch_with_report(self,report_file, id):
        self.do_ethtool(report_file,id)
