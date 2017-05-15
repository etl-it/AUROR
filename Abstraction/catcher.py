#Principal "class" of the Auror_Auditing_System

from __future__ import generators
import random
import os
import subprocess

import AurorTest
# from connectivity.py import Connectivity
# from devices.py  import Devices
# from architecture.py import Architecture


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


class Catcher(object):

    def __init__(self, tests_to_do, test_to_add):
        self.tests_to_do = tests_to_do
        self.done_tests = done_tests

    def add_Test(test_to_add):
        self.tests_to_do.append(test_to_add)

    def move_to_done(test_done):
        self.tests_to_do.remove(test_done)
        self.done_test.append(test_done)

    def clean_test_to_do():
        self.tests_to_do = []


    def clean_done_tests():
        self.done_tests = []

    pass


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


def main():
    print("main")

if __name__ == '__main__':
    main()
