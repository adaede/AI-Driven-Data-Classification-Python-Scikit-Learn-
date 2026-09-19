# src/aws_monitor.py
import boto3  # pyright: ignore[reportMissingImports]

def get_ec2_cpu_usage():
    cloudwatch = boto3.client("cloudwatch")
    ec2 = boto3.client("ec2")

    instances = ec2.describe_instances()
    instance_ids = [
        i["InstanceId"]
        for r in instances["Reservations"]
        for i in r["Instances"]
    ]

    for instance_id in instance_ids:
        metrics = cloudwatch.get_metric_statistics(
            Namespace="AWS/EC2",
            MetricName="CPUUtilization",
            Dimensions=[{"Name": "InstanceId", "Value": instance_id}],
            StartTime=pd.Timestamp.utcnow() - pd.Timedelta("1h"),
            EndTime=pd.Timestamp.utcnow(),
            Period=300,
            Statistics=["Average"],
        )
        datapoints = metrics.get("Datapoints", [])
        if datapoints:
            avg_cpu = datapoints[-1]["Average"]
            print(f"Instance {instance_id} CPU: {avg_cpu:.2f}%")

if __name__ == "__main__":
    import pandas as pd
    get_ec2_cpu_usage()
