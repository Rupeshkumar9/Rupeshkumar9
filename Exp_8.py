# A Python Program to Implement Priority Scheduling and show waiting time vs turnaround time
# Priority Scheduling 
# Input: Process ID, Burst Time, Priority

n = int(input("Enter total number of processes: "))
processes = []
for i in range(n):
    print(f"\nProcess {i+1}:")
    bt = int(input("Enter Burst Time: "))
    pr = int(input("Enter Priority (lower number = higher priority): "))
    processes.append([i+1, bt, pr])

# Sort processes by priority
processes.sort(key=lambda x: x[2])

# Initialize time lists
waiting_time = [0] * n
turnaround_time = [0] * n

# Calculate waiting and turnaround times
for i in range(1, n):
    waiting_time[i] = waiting_time[i-1] + processes[i-1][1]

for i in range(n):
    turnaround_time[i] = waiting_time[i] + processes[i][1]

# Display results
print("\nProcess\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"P{processes[i][0]}\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

# Calculate averages
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")

