import subprocess
import shlex

#subprocess works with additional processes
#shlex is for lexical analysis of shell-style syntaxes

#subprocess.Popen
#to run a process and read all of its output, set the stdout value to PIPE and call communicate()

#this script will wait for the process to complete and the it will display the output
#what we dp is reading the stdout line by line and display it in the console until it completes the process

#poll() => it returns the exit code if the process is completed or none if the process is still running


def catch_lspci():
    process = subprocess.Popen(shlex.split('lspci'), stdout = subprocess.PIPE)

    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print output.strip()

    rc = process.poll()
    return rc


def main():

    print catch_lspci()

if __name__ == '__main__':
    main()
