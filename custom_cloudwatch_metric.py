import subprocess
import boto3

output = subprocess.check_output('df -h | grep /dev/nvme | awk \'{print $5}\'', shell=True)
metric = float(output.decode('utf-8').strip().strip('%'))/100
print (metric)

client = boto3.client('cloudwatch')
response = client.put_metric_data(
    Namespace = 'my_custom_metric',
    MetricData = [
        {
            'MetricName': 'DiskUsage',
            'Dimensions':[
                {
                    'Name': 'DiskUsage',
                    'Value': '/'
                }
            ],
            'Value': metric
        }
    ]
)
