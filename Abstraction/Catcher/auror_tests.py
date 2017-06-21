

from Connectivity import connectivity
from Architecture import architecture
from Devices import devices


def available_tests():
    print """
        1 => Connectivity
        2 => Architecture
        3 => Devices
        .
        .
        .
    """

def sort(test):
    type = ""

    possible_mix_tests = ["Connectivity"]
    possible_hardware_tests = ["Devices", "hola", "adios"]
    possible_software_tests = ["Architecture", "venga", "funciona"]

    for i in possible_mix_tests:
        i_index = possible_mix_tests.index(i)
        if test == possible_mix_tests[i_index]:
            type = "MIX"
        else:
            pass
    for j in possible_hardware_tests:
        j_index = possible_hardware_tests.index(j)
        if test == possible_hardware_tests[j_index]:
            type = "HARDWARE"
        else:
            pass
    for k in possible_software_tests:
        k_index = possible_software_tests.index(k)
        if test == possible_software_tests[k_index]:
            type = "SOFTWARE"
        else:
            pass
    return type
