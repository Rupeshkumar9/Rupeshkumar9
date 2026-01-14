#  A Python program to list the top 5 running processes (process name + PID).

import psutil

# Get all running processes
processes = []
for proc in psutil.process_iter(['pid', 'name']):
    try:
        # Append each process info to the list
        processes.append(proc.info)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

# Print top 5 processes
print("------ Top 5 Running Processes ------")
for proc in processes[:5]:
    print(f"Process Name: {proc['name']}, PID: {proc['pid']}")






