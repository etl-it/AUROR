import sys, os, subprocess, shlex, commands

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


    my_packages = []

    linea = ''

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







def main():

    my = catch_packages()

    my_i = formate(my)

    p_install = my_i[0]

    p_deinstall = my_i[1]

    compare(p_install)

    package = 'apache2'

    dates = version('apache2')

    ver = dates[2]

    print("Version of "+ package + " is " + ver)








if __name__ == '__main__':
    main()
