from Catcher import catcher
from functions import *
from Connectivity import config_connectivity

class Connectivity(MixCatcher):

    def __init__(self, id):
        MixCatcher.__init__(self, "Connectivity", id)

    def getId(self, MixCatcher):
        return MixCatcher.getId()


    def ping_output_code(self, hostname):

        output_code = subprocess.call(['ping', '-c', '5', '-w', '15', hostname],
        stdout = open(os.devnull,'w'),
        stderr = open(os.devnull,'w'))
        return output_code

    def verify_host_list(self, host_list, report_file, id):

        return_output_codes = dict()

        report_to_print = []

        format1(id,report_to_print)

        for hostname in host_list:

            return_output_codes[hostname] = self.ping_output_code(hostname)

            format2(report_to_print)

            if return_output_codes[hostname] == 0:
                s = "HOSTNAME: " + hostname + " => OK "
                print(s)
                report_to_print.append(s)
                format2(report_to_print)
            else:
                s = "HOSTNAME: " ,hostname, " => ERROR "
                print(s)
                report_to_print.append(s)
                format2(report_to_print)

        if report_file != "no_report.txt":

            with open(report_file, 'a') as fichero:
                for s in report_to_print:
                    fichero.write(s + '\n')
                fichero.close()

    def catch(self,report_file, id):

        host_to_test = select_hosts()

        try:
            self.verify_host_list(host_to_test)
        except:
            print """ERROR"""
            sys.exit(2)
