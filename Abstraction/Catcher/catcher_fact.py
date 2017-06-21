from Catcher import auror_tests
from Connectivity.connectivity import Connectivity
from Architecture.architecture import Architecture
from Devices.devices import Devices

class CatcherFactory:
    def getSoftwareCatcher(self, name, id): pass
    def getHardwareCatcher(self, name, id): pass
    def getMixCatcher(self, name, id): pass

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
