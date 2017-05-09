#Principal "class" of the Auror_Auditing_System

from __future__ import generators

class CatcherFactory(object):

    factories = {}

    def addFactory(id, catcherFactory):
        CatcherFactory.factories.put[id] = catcherFactory
    addFactory = staticmethod(addFactory)

    def createCatcher(id):
        if not CatcherFactory.factories.has_key(id):
            CatcherFactory.factories[id] = \
                eval(id + '.Catcher()')
        return CatcherFactory.factories[id].create()
    createCatcher = staticmethod(createCatcher)


class Catcher(object): pass

class Hardware(Catcher):

    class Factory:
        def create(self): return Hardware()#Insert code

class Software(Catcher):

    class Factory:
        def create(self): return Software()

class Mix(Catcher):

    class Factory:
        def create(self): return Mix()
