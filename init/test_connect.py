import subprocess, time

#class test_connect(test)

hosts = ('8.8.8.8', '163.117.144.243')

#-c count => Stop after sending count ECHO_REQUEST packets.
#  -W timeout => Time to wait for a response, in seconds.

def ping(host):
    aux = subprocess.call(['ping','-c','5','w','3',host]
        stdout = open('/dev/null', 'w'),
        stderr = open('/dev/null', 'w'))
    return aux == 0

def is_up():
    print "[%s] Checking if network is up..." % time.strftime("%Y-%m-%d %H:%M:%S")

    bad_hosts = []

    for ihost in hosts:
        if not ping(ihost):
            bad_hosts.append(ihost)
            print "[%s] is unreacheable" %ihost

    return bad_hosts
