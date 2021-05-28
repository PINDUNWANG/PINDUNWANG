import subprocess
import re

def checkip(ip):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)')
    if p.match(ip):
        return True
    else:
        return False
def ipaccpas(s):
    pattern = re.compile('[^\x00]+')
    result = pattern.findall(s)
    return result
count = 0
myls = subprocess.Popen("ls ./dat_in/*.dat", shell=True,stdout=subprocess.PIPE)
for ls_out in myls.stdout:
    filename = ls_out[8:-1]

    with open( './dat_in/'+filename, 'r') as f, open( './dat_out/'+filename[:-3]+'txt','w') as out_file:
        s = f.read()
        x = s.split('\x01')
        for xx in x:
            if checkip(xx):
                count += 1
                print xx
                ret = ipaccpas(xx)
                out_file.write( ret[0]+':'+ret[1]+':'+ret[2]+'\n')
