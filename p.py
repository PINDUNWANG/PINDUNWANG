import subprocess

myls = subprocess.Popen("ls ./in/*.dat", shell=True,stdout=subprocess.PIPE)
for ls_out in myls.stdout:
    filename = ls_out[4:-1]

    with open( './in/'+filename, 'r') as dat_info, open( './out/'+filename,'w') as out_file:
        start_file = dat_info.read()
        #h = ''.join([hex(ord(x))[2:] for x in s])
        first_split = start_file.split('\x01')
        for second_split in first_split:
            if len(second_split) > 150:
                out = second_split.split('\x00')
                #print out
                cou = 0
                ip = []
                for _ in out:
                    if len(_)>1:
                        ip.append(_)
                        cou = cou + 1
                        if cou==3:
                            break
                if len(ip) == 3:
                    out_file.write( ip[0]+':'+ip[1]+':'+ip[2]+'\n')
