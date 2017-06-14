import subprocess
import os
import sys
import shlex

class Catcher:
    __type = ""
    __name = ""

    def __init__(self, type, name, id):
        self.__type = type
        self.__name = name

    def getType(self):
        return self.__type

    def getName(self):
        return self.__name

    def getId(self):
        return self.__id

class HardwareCatcher(Catcher):
    def __init__(self, name, id):
        Catcher.__init__(self, "Hardware", name, id)
    def getId(self):
        return Catcher.getId()
    def catch(self): pass
    def catch_with_report(self, report_file, id): pass

class SoftwareCatcher(Catcher):
    def __init__(self,name, id):
        Catcher.__init__(self, "Software", name, id)
    def getId(self):
        return Catcher.getId()
    def catch(self): pass
    def catch_with_report(self,report_file, id): pass

class MixCatcher(Catcher):
    def __init__(self, name, id):
        Catcher.__init__(self, "Mix", name, id)
    def getId(self):
        return Catcher.getId()
    def catch(self): pass
    def catch_with_report(self, report_file, id): pass

class CatcherFactory:
    def getSoftwareCatcher(self, name, id): pass
    def getHardwareCatcher(self, name, id): pass
    def getMixCatcher(self, name, id): pass

def print_test_title(id):
    s = "Report of test" + str(id)
    return s

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
            print('\n')
            print(test_title)
            salt = '\n'
            st_pre = """**************************************""" +'\n'
            print """**************************************"""

            report_to_print.append(salt)
            report_to_print.append(test_title)
            report_to_print.append(st_pre)

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

            with open(report_file, 'a') as fichero:
                for s in report_to_print:
                    fichero.write(s + '\n')
                fichero.close()


    def verify_host_list(self, host_list):
        return_output_codes = dict()

        print('\n')
        print(test_title)
        print """**************************************"""

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

class SoftwareCatcherFactory(CatcherFactory):
    def getSoftwareCatcher(self, name, id):
        if name == "Architecture":
            return Architecture(id)
        elif name == "Ethtool":
            return Ethtool(id)


class HardwareCatcherFactory(CatcherFactory):
    def getHardwareCatcher(self,name,id):
        if name == "Devices":
            return Devices(id)

class MixCatcherFactory(CatcherFactory):
    def getMixCatcher(self,name, id):
        if name == "Connectivity":
            return Connectivity(id)
