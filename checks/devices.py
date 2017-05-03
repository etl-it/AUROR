import subprocess
import shlex

#subprocess works with additional processes
#shlex is for lexical analysis of shell-style syntaxes

#subprocess.Popen
#to run a process and read all of its output, set the stdout value to PIPE and call communicate()

#this script ĺl wait for the process to complete and the it will display the output
#what we dp is reading the stdout line by line and display it in the console until it completes the process

#poll() => it returns the exit code if the process is completed or none if the process is still running


def catch_lspci():
    process = subprocess.Popen('lspci', stdout = subprocess.PIPE)
    stdout = process.communicate()[0]
    print 'STDOUT:{}'.format(stdout)

    output = process.stdout.readLine()

    process.poll()


    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print output.strip()

        rc = process.poll()


        http://blog.endpoint.com/2015/01/getting-realtime-output-using-python.html
