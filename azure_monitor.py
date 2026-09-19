# src/azure_monitor.py
from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient
from datetime import datetime, timedelta

SUBSCRIPTION_ID = "YOUR_SUBSCRIPTION_ID"

def get_vm_cpu_usage():
    credential = DefaultAzureCredential()
    monitor_client = MonitorManagementClient(credential, SUBSCRIPTION_ID)

    # Example: replace with your resource ID
    resource_id = "/subscriptions/XXXX/resourceGroups/XXXX/providers/Microsoft.Compute/virtualMachines/XXXX"

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=1)

    metrics_data = monitor_client.metrics.list(
        resource_id,
        timespan=f"{start_time}/{end_time}",
        interval="PT5M",
        metricnames="Percentage CPU",
        aggregation="Average",
    )

    for item in metrics_data.value:
        for timeseries in item.timeseries:
            for data in timeseries.data:
                if data.average is not None:
                    print(f"CPU: {data.average:.2f}% at {data.time_stamp}")

if __name__ == "__main__":
    get_vm_cpu_usage()
