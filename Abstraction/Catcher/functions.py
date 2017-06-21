import random

def rep(num, usados):
    repetido = False
    for i in usados:
        if num == usados[i]:
            repetido = True
    return repetido


def print_test_title(id):
    s = "Report of test" + str(id)
    return s


def generate_id(cantidad, min, max, usados):

    if max < min:
        min, max = max, min

    if cantidad > (max-min):
        print "solamente puedo generar %d numeros" % (max-min)
        cantidad = max - min

    num = random.randint(min, max)

    repe = rep(num, usados)
    while (repe == False):
        num = random.randint(min, max)

    usados.append(num)

    return num

def format1(id, report_to_print):

        test_title = print_test_title(id)
        print('\n')
        print(test_title)
        salt = '\n'
        st_pre = """**************************************""" +'\n'
        print """**************************************"""

        report_to_print.append(salt)
        report_to_print.append(test_title)
        report_to_print.append(st_pre)

def format2(report_to_print):

    print """-----------------------------------"""
    st = """-----------------------------------"""
    report_to_print.append(st)
