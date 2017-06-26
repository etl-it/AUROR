import sys, os, subprocess
from Catcher import catcher
from Catcher.functions import format1, format2

class App(catcher.SoftwareCatcher):

    def __init__(sef,id):
        catcher.SoftwareCatcher.__init__(self, "Architecture",id)

    def getId(self, SoftwareCatcher):
        return catcher.SoftwareCatcher.getId()

    def version(package):

        process = subprocess.Popen(shlex.split('dpkg -s ' + package),
                                stdout = subprocess.PIPE,
                              )

        i = 0
        find = False
        name = ''
        status = ''
        ver = ''


        while find is False:

            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break

            if i == 0:
                name = output[:-1]
            elif i == 1:
                status = output[:-1]
            elif i == 7:
                ver = output[:-1]
                find = True

            i = i + 1

        rc = process.poll()

        dates = [name, status, ver]

        return dates

    #TENGO QUE DEFINIR ESTE METODO SOLO CON REPORT FILE E ID NECESARIAMENTE
    def catch(self,report_file, id):

        packege = select_package()

        self.version(package)
