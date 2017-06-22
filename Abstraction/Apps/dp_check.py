import sys, os, subprocess, shlex

def catch_packages():

    my_packages = []

    process = subprocess.Popen(shlex.split('dpkg --get-selections'),
                                stdout = subprocess.PIPE,
                              )

    for i in range(1,100000):
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
             my_packages.append(output)

    rc = process.poll()

    return my_packages

def formate(my_packages):

    my_packages_install = []
    my_packages_deinstall = []

    for line in my_packages:
        if 'deinstall' in line:
            index = my_packages.index(line)
            my_packages.pop(index)
            index = line.find('\t')
            pretty_line = line[0:index]

            my_packages_deinstall.append(pretty_line)

    for line in my_packages:
        index = line.find('\t')
        pretty_line = line[0:index]
        my_packages_install.append(pretty_line)

    return [my_packages_install, my_packages_deinstall]



def compare(list):
    file_to_verify = '/usr/lab/alum/0330717/AUROR/Abstraction/Apps/TxtFiles/peque_lista.txt'

    elements_to_verify = []

    infile = open(file_to_verify, 'r')
    for line in infile:
        elements_to_verify.append(line)
    infile.close()

    is_in = []

    for j in range(0, len(list)):
        for i in range(0, len(elements_to_verify)):
            #print(list[j],elements_to_verify[i])

            if list[j]+'\n' == elements_to_verify[i]:

                is_in.append(list[j])
                print list[j]

                ##ESCRIBIR ALGUNA INFO AQUI

def version(package):

    info = []

    ##PROBAR OTROS PORQUE LA FORMA QUE TE LO LISTA ES MUY RARRA
    process = subprocess.Popen(shlex.split('dpkg -l ' + package),
                                stdout = subprocess.PIPE,
                              )

    for i in range(1,100):
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            info.append(output)

    rc = process.poll()

    print info



def main():

    my = catch_packages()

    my_i = formate(my)

    p_install = my_i[0]

    p_deinstall = my_i[1]

    compare(p_install)

    version('acpid')








if __name__ == '__main__':
    main()
