import subprocess
import os
import sys

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

class HardwareCather(Catcher):
    def __init__(self, name, id):
        Catcher.__init__(self, "Hardware", name, id)
    def catch(self): pass
    def catch_with_report(self, id): pass

class SoftwareCather(Catcher):
    def __init__(self,name, id):
        Catcher.__init__(self, "Software", name, id)
    def catch(self): pass
    def catch_with_report(self, id): pass

class MixCatcher(Catcher):
    def __init__(self, name, id):
        Catcher.__init__(self, "Mix", name, id)
    def catch(self): pass
    def catch_with_report(self, id): pass

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


    #Metodos Propios
    def ping_output_code(self, hostname):

        output_code = subprocess.call(['ping', '-c', '5', '-w', '15', hostname],
        stdout = open(os.devnull,'w'),
        stderr = open(os.devnull,'w'))
        return output_code

    def verify_host_list_report(self, host_list, report_file, id):

        return_output_codes = dict()

        if report_file != "no_report.txt":

            test_title = print_test_title(id)

             with open(report_file, 'w') as archivo:

                archivo.write(test_title)

                for hostname in host_list:
                    return_output_codes[hostname] = self.ping_output_code(hostname)
                    print """-----------------------------------"""
                    st = """-----------------------------------"""
                    archivo.write(s)
                    if return_output_codes[hostname] == 0:
                        s = "HOSTNAME: " + hostname + " => OK "
                        print(s)
                        archivo.write(s)
                        archivo.write(st)
                    else:
                        s = "HOSTNAME: " ,hostname, " => ERROR "
                        archivo.write(s)
                        archivo.write(st)
            archivo.close()

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
            self.verify_host_list_report(host_to_test)
        except:
            print """ERROR"""
            sys.exit(2)

class Architecture(SoftwareCather):
    #"CONSTRUCTOR"
    def __init__(self, id):
        SoftwareCather.__init__(self, "Architecture",id)

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
            try:
                s = self.define_architecture())
                test_title = print_test_title(id)

                with open(report_file, 'w') as archivo:

                    archivo.write(test_title)
                archivo.close()

            except:
                print """ERROR"""
                sys.exit(2)


class SoftwareCatcherFactory(CatcherFactory):
    def getSoftwareCatcher(self, name, id):
        if name == "Architecture":
            return Architecture(pasarleid)


class HardwareCatcherFactory(CatcherFactory): pass

class MixCatcherFactory(CatcherFactory):
    def getMixCatcher(self,name, id):
        if name == "Connectivity":
            return Connectivity(pasarleid)
