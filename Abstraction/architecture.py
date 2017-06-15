class Architecture(SoftwareCatcher):
    #"CONSTRUCTOR"
    def __init__(self, id):
        SoftwareCatcher.__init__(self, "Architecture",id)

    def getId(self, MixCatcher):
        return SoftwareCatcher.getId()

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

    #Metodo para generalizacion con factoria
    def catch(self):
        try:
            print(self.define_architecture())
        except:
            print """ERROR"""
            sys.exit(2)

    def catch_with_report(self,report_file, id):

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
            report_to_print.append(st_pre)
            s = self.define_architecture()
            print(s)
            report_to_print.append(s)

            with open(report_file, 'a') as fichero:
                for s in report_to_print:
                    if s != None:
                        s = str(s)
                        fichero.write(s + '\n')
                fichero.close()
