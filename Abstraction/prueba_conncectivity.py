import os
import subprocess



def ping_output_code(hostname):

    output_code = subprocess.call(['ping', '-c', '5', '-w', '15', hostname],
    stdout = open(os.devnull,'w'),
    stderr = open(os.devnull,'w'))
    return output_code

def verify_host_list(host_list):

    return_output_codes = dict()

    for hostname in host_list:
        return_output_codes[hostname] = ping_output_code(hostname)
        print hostname
        print """\t"""
        if return_output_codes[hostname] == 0:
            print("OK")
            print """\t"""
        else:
            print("ERROR")
            print """\t"""

    return return_output_codes


def main():
    host_to_test = ['google.com',
                    '163.117.144.243', ##alcazar01.lab.it.uc3m.es
                    '163.117.168.105'
                    ]
    verify_host_list(host_to_test)

if __name__ == '__main__':
    main()
