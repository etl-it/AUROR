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

class SoftwareCather(Catcher):
    def __init__(self,name):
        Catcher.__init__(self, "Software", name)

class MixCatcher(Catcher):
    def __init__(self, name):
        Cather.__init__(self, "Mix", name)

######

class Architecture(Software):
    def __init__(self):
        SoftwareCather.__init__(self, "Software")

class Connectivity(MixCatcher):
    def __init__(self):
        MixCatcher.__init__(self, "Connectivity")


#Abstract factory class
class CatcherFactory:
    def getSoftwareCatcher(self, name): pass
    def getHardwareCatcher(self, name): pass
    def getMixCatcher(self, name): pass

class SoftwareCatcherFactory(CatcherFactory):
    def getSoftwareCatcher(self, "Architecture"):
        return Architecture()
class HardwareCatcherFactory(CatcherFactory): pass

class MixCatcherFactory(CatcherFactory):
    def getMixCatcher(self, "Connectivity"):
        return Connectivity()
