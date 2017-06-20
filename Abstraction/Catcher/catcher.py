
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
    def catch(self,report_file, id): pass

class SoftwareCatcher(Catcher):
    def __init__(self,name, id):
        Catcher.__init__(self, "Software", name, id)
    def getId(self):
        return Catcher.getId()
    def catch(self,report_file, id): pass

class MixCatcher(Catcher):
    def __init__(self, name, id):
        Catcher.__init__(self, "Mix", name, id)
    def getId(self):
        return Catcher.getId()
    def catch(self,report_file, id): pass
