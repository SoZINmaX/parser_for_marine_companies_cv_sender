#!/usr/bin/python

import subprocess
subprocess.run("./sleep.sh", shell=True)
subprocess.run('sudo chown -R root' + 'directrory_for_chown', shell = True, capture_output=True)
directrory_for_chown = str(directory1.stdout)
print(directrory_for_chown)
subprocess.run(['sudo chown -R root' + ' ' + directory_for_chown], shell = True, capture_output=True)
create_dz1 = subprocess.run(['touch dz1.py', 'ls'] , shell = True, capture_output=True)

create_dr1_run = subprocess.run(['touch dz1_run.py', 'ls'] , shell = True, capture_output=True)
copyfile = subprocess.run(['shutil.copyfile' + "('" + directory_decoded + "dz1.py', '" + directory_decoded + 'dz1_run.py' +"')" ] , shell = True, capture_output=True)
owner_can_read_run = subprocess.run(['chmod u+rx dz1_run.py'] , shell = True)


#!/usr/bin/python3
import subprocess

create_dz1 = subprocess.run(['touch dz1.py', 'ls'] , shell = True)

create_dr1_run = subprocess.run(['touch dz1_run.py', 'ls'] , shell = True)

copyfile = subprocess.run(['cat dz1.py > dz1_run.py'] , shell = True)

deny_all_except_owner = subprocess.run(['chmod ugo-rwx dz1_run.py'] , shell = True)