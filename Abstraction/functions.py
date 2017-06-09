import random

def rep(num, usados):
    repetido = false
    for i in usados:
        if num == usados[i]:
            repetido = True
    return repetido


def generate_id(cantidad, min, max, usados):

    if max < min:
        min, max = max, min

    if cantidad > (max-min):
        print "solamente puedo generar %d numeros" % (max-min)
        cantidad = max - min

    num = random.randint(min, max)

    repe = rep(num)
    while (repe == False):
        num = random.randint(min, max)

    usados.append(num)

    return num
