import subprocess
import os
import sys

class Catcher:
    __type = ""
    __name = ""

    def __init__(self, type, name):
        self.__type = type
        self.__name = name

    def getType(self):
        return self.__type

    def getNmae(self):
        return self.__name

class HardwareCather(Catcher):
    def __init__(self, name):
        Catcher.__init__(self, "Hardware", name)
    def catch(self,params): pass

class SoftwareCather(Catcher):
    def __init__(self,name):
        Catcher.__init__(self, "Software", name)
    def catch(self): pass #ESTO HAY QUE CAMBIARLO

class MixCatcher(Catcher):
    def __init__(self, name):
        Catcher.__init__(self, "Mix", name)
    def catch(self,params): pass

class CatcherFactory:
    def getSoftwareCatcher(self, name): pass
    def getHardwareCatcher(self, name): pass
    def getMixCatcher(self, name): pass

class Connectivity(MixCatcher):

    #"CONSTRUCTOR"
    def __init__(self):
        MixCatcher.__init__(self, "Connectivity")


    #Metodos Propios
    def ping_output_code(self, hostname):

        output_code = subprocess.call(['ping', '-c', '5', '-w', '15', hostname],
        stdout = open(os.devnull,'w'),
        stderr = open(os.devnull,'w'))
        return output_code

    def verify_host_list(self, host_list):

        return_output_codes = dict()

        for hostname in host_list:
            return_output_codes[hostname] = self.ping_output_code(hostname)
            print hostname
            print """\t"""
            if return_output_codes[hostname] == 0:
                print("OK")
                print """\t"""
            else:
                print("ERROR")
                print """\t"""

    #Metodo para generalizacion con factoria
    def catch(self,params): #params = host_list
        try:
            self.verify_host_list(params)
        except:
            print """ERROR"""
            sys.exit(2)

class Architecture(SoftwareCather):
    #"CONSTRUCTOR"
    def __init__(self):
        SoftwareCather.__init__(self, "Architecture")

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
            self.define_architecture()
        except:
            print """ERROR"""
            sys.exit(2)

class SoftwareCatcherFactory(CatcherFactory):
    def getSoftwareCatcher(self, name):
        if name == "Architecture":
            return Architecture()


class HardwareCatcherFactory(CatcherFactory): pass

class MixCatcherFactory(CatcherFactory):
    def getMixCatcher(self,name):
        if name == "Connectivity":
            return Connectivity()
