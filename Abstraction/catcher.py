#import connectivity

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
    def catch(self,params): pass

class MixCatcher(Catcher):
    def __init__(self, name):
        Cather.__init__(self, "Mix", name)
    def catch(self,params): pass

######

class Architecture(SoftwareCather):
    def __init__(self):
        SoftwareCather.__init__(self, "Software")

class Connectivity(MixCatcher):
    def __init__(self):
        MixCatcher.__init__(self, "Connectivity")


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
            if return_output_codes == 0:
                print("OK")
            else:
                print("ERROR")

        return return_output_codes

        def catch(self,params): #params = host_list
                verify_host_list(params)



# class Connectivity(MixCatcher):
#     def __init__(self):
#         MixCatcher.__init__(self, "Connectivity")


#Abstract factory class
class CatcherFactory:
    def getSoftwareCatcher(self, name): pass
    def getHardwareCatcher(self, name): pass
    def getMixCatcher(self, name): pass


class SoftwareCatcherFactory(CatcherFactory):
    def getSoftwareCatcher(self, name):
        if name == "Architecture":
            return Architecture()


class HardwareCatcherFactory(CatcherFactory): pass

class MixCatcherFactory(CatcherFactory):
    def getMixCatcher(self,name):
        if name == "Connectivity":
            return Connectivity()
