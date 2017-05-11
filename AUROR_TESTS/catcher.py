#Principal "class" of the Auror_Auditing_System

from __future__ import generators
import random

class CatcherFactory:

    factories = {}

    def addFactory(id, catcherFactory):
        CatcherFactory.factories.put[id] = catcherFactory
    addFactory = staticmethod(addFactory)

    def createCatcher(id):
        if not CatcherFactory.factories.has_key(id):
            CatcherFactory.factories[id] = \
                eval(id + '.Factory()')
        return CatcherFactory.factories[id].create()
    createCatcher = staticmethod(createCatcher)


class Catcher(object): pass

class Hardware(Catcher):

    def one_check(test_to_check): print("This make one hardware test")
    def check_all(): print("This make all the hardware tests")

    class Factory:
        def create(self): return Hardware()

class Software(Catcher):

    def one_check(test_to_check): print("This make a one Software test")
    def check_all(): print("This make all the Software tests")

    class Factory:
        def create(self): return Software()

class Mix(Catcher):

    def one_check(test_to_check): print("This make one Mix test")
    def check_all(): print("This make all the Mix tests")


    class Factory:
        def create(self): return Mix()


def catherNameGen(n):

    times = 7

    test_to_check = "This"

    types = Catcher._subclasses_()

    for i in range(n):
        yield random.choice(types).__name__

    catchers = [CatcherFactroy.createCatcher(i)
                for i in cathcerNameGen(times)]

    for catcher in catchers:
        catcher.one(test_to_check)
