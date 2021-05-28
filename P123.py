import subprocess
import re

def checkip(ip):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(ip):
        return True
    else:
        return False


mystrings = subprocess.Popen("strings -n 1 ./in/*.dat", shell=True,stdout=subprocess.PIPE)
with open( './out/test.txt','w') as out_fite:
    ips = []
    ip = ''
    for _out in mystrings.stdout:
        #print _out[:-1]
        if checkip(_out):
            ip =   _out + next(mystrings.stdout) + next(mystrings.stdout)
            ip = ip.replace('\n',':')[:-1]
            if ip not in ips:
                ips.append(ip)
                out_file.write(ip+'\n')

