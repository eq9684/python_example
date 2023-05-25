import subprocess
import sys
import boto3

output = subprocess.check_output('ps -ef | grep ' + str(sys.argv[1]) + ' | grep -v grep | grep -v check_proc | awk \'{print $2}\'', shell=True)
metric = output.decode('utf-8').strip().strip('%')
if metric == '':
    print ('process not exist')
else:
    print ('process id is ' + metric)
