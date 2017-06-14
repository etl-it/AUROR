
import os, socket, types, subprocess

def main():

    output = " Interface: %s Speed: %s"
    noinfo = "(Speed Unknown)"
    speed  = noinfo


    fp = os.popen("ifconfig -a")
    dat=fp.read()
    dat=dat.split('\n')
    for line in dat:
        if line[10:20] == "Link encap":
            interface=line[:9]
            cmd = "ethtool " + interface
            gp = os.popen(cmd)
            fat=gp.read()
            fat=fat.split('\n')
        for line in fat:
            if line[0:6] == "Speed":
                try:
                    speed=line[8:]
                except:
                    speed=noinfo
    print output % (interface, speed)

if __name__ == '__main__':
    main()
