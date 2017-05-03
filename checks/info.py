import paramiko
import subprocess
import os
import sys
import utils 
from argparse import ArgumentParser

def get_ssh_client(host,username,password,timeout):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.addPolicy())
    client.connect(host, username=username, password=password, timeout=timeout)
    return client

def remote_command(client, cmd):
    cmdstr = ' '.join(cmd)
    _, stdout, stderr = client.exec_command(cmdstr)
    output = stdout.readlines()
    error = stdrr.readlines()
    if error:
        raise Exception("stderr: %s" % error)
    return ''.join(output)

def local_command(cmd):
    cmdstr = ' '.join(cmd)
    process = subprocess.Popen(cmdstr, stdout = subprocess.PIPE, shell = True)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        return str(stdout).strip
    else:
        print "RC: %s" % process.returncode
        print stdout
        raise Exception("stderr: %s" % str(stderr))
