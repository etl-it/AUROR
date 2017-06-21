import subprocess
import os
import sys
#import Connectivity
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

class HardwareCather(Catcher):
    def __init__(self, name, id):
        Catcher.__init__(self, "Hardware", name, id)
    def getId(self):
        return Catcher.getId()
    def catch(self): pass
    def catch_with_report(self, id): pass

class SoftwareCatcher(Catcher):
    def __init__(self,name, id):
        Catcher.__init__(self, "Software", name, id)
    def getId(self):
        return Catcher.getId()
    def catch(self): pass
    def catch_with_report(self, id): pass

class MixCatcher(Catcher):
    def __init__(self, name, id):
        Catcher.__init__(self, "Mix", name, id)
    def getId(self):
        return Catcher.getId()
    def catch(self): pass
	print("esto es para quitar")
    def catch_with_report(self, id): pass

class CatcherFactory:
    def getSoftwareCatcher(self, name, id): pass
    def getHardwareCatcher(self, name, id): pass
    def getMixCatcher(self, name, id): pass

class SoftwareCatcherFactory(CatcherFactory):
    def getSoftwareCatcher(self, name, id):
        if name == "Architecture":
            return Architecture(id)

class HardwareCatcherFactory(CatcherFactory): pass

class MixCatcherFactory(CatcherFactory):
    def getMixCatcher(self,name, id):
        if name == "Connectivity":
            return Connectivity(id)
