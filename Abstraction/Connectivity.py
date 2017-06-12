from catcher import *

class Connectivity(MixCatcher):

    #"CONSTRUCTOR"
    def __init__(self, id):
        MixCatcher.__init__(self, "Connectivity", id)

    def getId(self, MixCatcher):
        return MixCatcher.getId()


    #Metodos Propios
    def ping_output_code(self, hostname):

        output_code = subprocess.call(['ping', '-c', '5', '-w', '15', hostname],
        stdout = open(os.devnull,'w'),
        stderr = open(os.devnull,'w'))
        return output_code

    def verify_host_list_report(self, host_list, report_file, id):

        return_output_codes = dict()

        report_to_print = []

        if report_file != "no_report.txt":

            test_title = print_test_title(id)
            report_to_print.append(test_title)

            for hostname in host_list:
                return_output_codes[hostname] = self.ping_output_code(hostname)
                print """-----------------------------------"""
                st = """-----------------------------------"""
                report_to_print.append(st)
                if return_output_codes[hostname] == 0:
                    s = "HOSTNAME: " + hostname + " => OK "
                    print(s)
                    report_to_print.append(s)
                    report_to_print.append(st)
                else:
                    s = "HOSTNAME: " ,hostname, " => ERROR "
                    report_to_print.append(s)
                    report_to_print.append(st)

            with open(report_file, 'w') as fichero:
                for s in report_to_print:
                    fichero.write(s + '\n')
                fichero.close()


    def verify_host_list(self, host_list):
        return_output_codes = dict()

        for hostname in host_list:
            return_output_codes[hostname] = self.ping_output_code(hostname)
            print """-----------------------------------"""
            if return_output_codes[hostname] == 0:
                print("HOSTNAME: " + hostname + " => OK ")
                print """-----------------------------------"""
            else:
                print("HOSTNAME: " ,hostname, " => ERROR ")
                print """-----------------------------------"""

    #Metodo para generalizacion con factoria
    def catch(self): #params = host_list
        host_to_test = ['google.com',
                        '163.117.144.243', ##alcazar01.lab.it.uc3m.es
                        '163.117.168.105'
                        ]
        try:
            self.verify_host_list(host_to_test)
        except:
            print """ERROR"""
            sys.exit(2)

    def catch_with_report(self,report_file, id):
        host_to_test = ['google.com',
                        '163.117.144.243', ##alcazar01.lab.it.uc3m.es
                        '163.117.168.105'
                        ]
        try:
            self.verify_host_list_report(host_to_test, report_file, id)
        except:
            print """ERROR"""
            sys.exit(2)
