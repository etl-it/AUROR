import os
from COnfigParser import RawConfigParser

def mode():

    mode = raw_input('Select if you want an only-one check package or if you wanna check several: One/More')

    if mode.lower() == 'one' :
        select_one_pack()
    elif mode.lower() == 'more' :
        select_sev_pack()
    else:
        break

def select_one_pack():

    pack = raw_input('Insert the name of te package you wanna check version of:')

    return pack



def select_sev_pack():

    pack_tests = []

    end = False

    while end is False:

        pack = raw_input('Insert the name of the pakages you wanna check. When you finish the selection write END:')

        pack_tests.append(pack)

        if pack == "END":
            pack_tests.remove(pack)
            end = True

    return pack_tests
