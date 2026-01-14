# A Python Program to Implement First Come First Serve (FCFS) CPU scheduling in Python.

# Input number of processes
n = int(input("Enter number of processes: "))

# Lists to store burst time, waiting time, and turnaround time
bt = []
wt = [0] * n
tat = [0] * n

# Input burst times
for i in range(n):
    bt.append(int(input(f"Enter burst time for process {i+1}: ")))

# Calculate waiting times
for i in range(1, n):
    wt[i] = wt[i-1] + bt[i-1]

# Calculate turnaround times
for i in range(n):
    tat[i] = wt[i] + bt[i]

# Display results
print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"P{i+1}\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")



    