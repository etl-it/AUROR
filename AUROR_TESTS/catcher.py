#Principal "class" of the Auror_Auditing_System

from __future__ import generators

#INternal classes are nested whithin the factory method to disallow direct access to them
class Catcher(object):
    #
    # types_catcher = []
    #
    # #Create based on class name => Posibles modificaciones para mejor adaptación
    # def factory(type):
    #         class Hardware(Catcher):
    #             #Insert code
    #
    #         class Software(Catcher):
    #             #Insert code
    #
    #         class Mix(Catcher):
    #             #Insert code
    #
    #         if type == "Hardware": return Hardware()
    #         if type == "Software": return Software()
    #         if type == "Mix": return Mix()
    #         assert 0, "Bad Catcher Test creation: " + type


#Use of PLOYMORFHIC FACTORIES. By this way, different types of factories can be subclassed from
#the basic factory


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
        def create(self): return Hardware()

class Software(Catcher):

    class Factory:
        def create(self): return Software()

class Mix(Catcher):

    class Factory:
        def create(self): return Mix()
