import os
import subprocess

class Test(object):

    def __init__ (self, id, description, type):
        self.id = id
        self.description = description
        self.type = type

    def getId():
        return self.id

    def getDescription():
        return self.description

    def getType():
        return self.type

    #No hacen falta setters en Python; se puede modificar directamente el atributo de un objeto sin necesidad de usar un método
