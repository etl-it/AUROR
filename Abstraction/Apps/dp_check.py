import sys, os, subprocess

def catch_packages():
    process = subprocess.Popen(['dpkg', '--get-selections'],
                                stdot = subprocess.PIPE,
                              )
    out_value = process.communicate()[0]

    
