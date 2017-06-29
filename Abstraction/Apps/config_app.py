import os
from ConfigParser import RawConfigParser

def mode():

    mode = raw_input('Select if you want an only-one check package or if you wanna check several: One/More >>')
    mode_opt = 0

    if mode.lower() == 'one' :
        select_one_pack()
        mode_opt = 1
    elif mode.lower() == 'more' :
        select_sev_pack()
        mode_opt = 2
    else:
        print("Invalid option")

    return mode_opt

def select_one_pack():

    pack = raw_input('Insert the name of te package you wanna check version of:>>')

    print pack
    return pack

def select_sev_pack():

    pack_tests = []

    end = False

    while end is False:

        pack = raw_input('Insert the name of the pakages you wanna check. When you finish the selection write END. >>')

        pack_tests.append(pack)

        if pack == "END":
            pack_tests.remove(pack)
            end = True

    return pack_tests


def config_app_conf(dir):

    current_dir = os.getcwd()
    config_app_conf = "/usr/lab/alum/0330717/Auror_workspace/app.conf"
    cparser = RawConfigParser()

    if current_dir != dir :
        os.chdir(dir)


    mode_opt = mode()

    print mode_opt

    pack_tests = []

    if mode_opt != 0:
        if mode_opt == 1:
            pack = select_one_pack()
            pack_tests.append(pack)
        elif mode_opt == 2:
            pack_tests = select_sev_pack()
        else:
            pass

    with open(config_app_conf, 'wb') as archivo:
        cparser.add_section("PACKAGES")
        for pack in pack_tests:
            pack_index = pack_tests.index(pack)
            pack_name = 'PACK' + str(pack_index)
            cparser.set("PACKAGES", pack_name, pack)
        cparser.write(archivo)

def main():
    dir = "/usr/lab/alum/0330717/Auror_workspace"
    config_app_conf(dir)

if __name__ == '__main__':
    main()
