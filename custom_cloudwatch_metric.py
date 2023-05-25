import subprocess
import boto3

hostname = subprocess.check_output('hostname', shell=True).decode('utf-8').strip()
output = subprocess.check_output('df -h | grep /dev/nvme | awk \'{print  $5}\'', shell=True)
metric = float(output.decode('utf-8').strip().strip('%'))/100
print (hostname)
print (metric)

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
        }
    ]
)
