# program to implement Banker’s Algorithm (Deadlock Avoidance)


alloc = [[1, 2], [2, 0], [3, 1]] # Allocation Matrix
maxm = [[3, 3], [3, 2], [4, 3]] # Max Matrix


avail = [2, 1] # Available Resources
n = len(alloc) # number of processes
m = len(avail) # number of resource types

need = [[maxm[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
finish = [False] * n
safe_seq = []


while len(safe_seq) < n:
    allocated_in_this_round = False


    for i in range(n):
        if not finish[i] and all(need[i][j] <= avail[j] for j in range(m)):
                avail = [avail[j] + alloc[i][j] for j in range(m)]
                finish[i] = True
                safe_seq.append(i)
                allocated_in_this_round = True


    if not allocated_in_this_round:
            break


if len(safe_seq) == n:
        print("Safe Sequence:", safe_seq)

else:
    print("System is in UNSAFE state")










