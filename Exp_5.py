# A Python program to display Monitor Network Statistics (Bytes Sent/Received).

import psutil

net_io = psutil.net_io_counters()

print(f"Bytes Sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB")
print(f"Bytes Received: {net_io.bytes_recv / (1024 ** 2):.2f} MB")



