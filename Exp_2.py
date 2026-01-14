# A Python program to show Disk Partitions and Usage.

import psutil

# Get all disk partitions
partitions = psutil.disk_partitions()

print("Disk Partitions and Usage:\n")
for partition in partitions:
    print(f"Device: {partition.device}")
    print(f"  Mountpoint: {partition.mountpoint}")
    print(f"  File system type: {partition.fstype}")
    try:
        # Get partition usage details
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"  Total Size: {usage.total / (1024**3):.2f} GB")
        print(f"  Used: {usage.used / (1024**3):.2f} GB")
        print(f"  Free: {usage.free / (1024**3):.2f} GB")
        print(f"  Percentage Used: {usage.percent}%\n")
    except PermissionError:
        # Sometimes permission errors occur on restricted partitions
        print("  Permission Denied\n")


