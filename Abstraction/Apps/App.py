import sys, os, subprocess
from Catcher import catcher
from Catcher.functions import format1, format2

class App(catcher.SoftwareCatcher):

    def __init__(sef,id):
        catcher.SoftwareCatcher.__init__(self, "Architecture",id)

    def getId(self, SoftwareCatcher):
        return catcher.SoftwareCatcher.getId()
