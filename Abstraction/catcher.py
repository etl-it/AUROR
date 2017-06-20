import subprocess
import os
import sys
import shlex

from auror_tests import *

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
