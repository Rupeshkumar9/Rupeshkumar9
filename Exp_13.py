# FCFS disk scheduling Algorithm.

# FCFS

def fcfs(requests, head):
    total = 0
    current = head
    print("Sequence:", end=" ")

    for req in requests:
        print(req, end=" ")
        total += abs(current - req)
        current = req

    print("\nTotal Head Movement:", total)

requests = [82, 170, 43, 140, 24, 16, 190]

head = 50
fcfs(requests, head)




# SSTF -

def sstf(requests, head):
    requests = requests.copy()
    total = 0
    current = head
    print("Sequence: ", end=" ")

    while requests:
        nearest = min(requests, key = lambda x: abs(x - current))
        print(nearest, end = " ")
        total += abs(current - nearest)
        current = nearest
        requests.remove(nearest)

    print("\nTotal Head Movement: ", total)

requests = [82, 170, 43, 140, 24, 16, 190]
head = 50
sstf(requests, head)
