import subprocess
import sys
import boto3

#usage: python3 check_proc.py process_name
output = subprocess.check_output('ps -ef | grep ' + str(sys.argv[1]) + ' | grep -v grep | grep -v report_proc | awk \'{print $2}\'', shell=True)
metric = output.decode('utf-8').strip().strip('%').split()
if len(metric) == 0:
    print ('process not exist')
else:
    print ('find ' + str(len(metric)) + ' processes, the first process id is ' + metric[0])
