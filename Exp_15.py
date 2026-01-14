# Simulate Container as a Scheduler.


requests = [55, 18, 98, 155, 38]
head = 50

print(" Head : ", head)
print("Requests : ", requests)



order = []
pending = requests.copy()

while pending:
    # Find the request with the minimum distance from the current head
    next_req = min(pending, key=lambda x: abs(x - head))
    
    order.append(next_req)
    head = next_req
    
    # This part is written vertically on the side in the image
    pending.remove(next_req)

print("Service order : ", order)


