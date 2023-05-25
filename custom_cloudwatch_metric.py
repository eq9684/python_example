import subprocess
import boto3

hostname = subprocess.check_output('hostname', shell=True).decode('utf-8').strip()
output = subprocess.check_output('df -h | grep /dev/nvme | awk \'{print $5}\'', shell=True)
metric = float(output.decode('utf-8').strip().strip('%'))/100
memfree = round(int(subprocess.check_output('cat /proc/meminfo | grep MemFree | awk \'{print $2}\'', shell=True).decode('utf-8').strip())/1024, 1)
print (hostname)
print (metric)
print (memfree, 'MB Memory Free')

client = boto3.client('cloudwatch')
response = client.put_metric_data(
    Namespace = 'my_custom_metric',
    MetricData = [
        {
            'MetricName': 'DiskUsage',
            'Dimensions':[
                {
                    'Name': hostname,
                    'Value': '/'
                }
            ],
            'Value': metric
        },
        {
            'MetricName': 'MemFree',
            'Dimensions':[
                {
                    'Name': hostname,
                    'Value': 'MemFree'
                }
            ],
            'Value': memfree
        }
    ]
)
