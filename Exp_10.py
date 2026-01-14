# Extend LRU with a prediction model (predict next reference using past data).

pages = [1, 2, 3, 2, 4, 1, 5, 2, 3, 4]
capacity = 3
memory = []
faults = 0

for i in range(len(pages)):
    page = pages[i]

    # if page not in memory -> page fault
    if page not in memory:
        faults += 1

        # if memory is full, predict which page won't be used soon
        if len(memory) == capacity:
            # dictionary to store next use index of each page in memory
            next_use = {}
            for p in memory:
                if p in pages[i+1:]:
                    next_use[p] = pages[i+1:].index(p)  # distance to next use
                else:
                    next_use[p] = float('inf')  # not used again
            
            # page with the farthest next use or never used again
            page_to_remove = max(next_use, key=next_use.get)
            memory.remove(page_to_remove)

        # add the new page
        memory.append(page)

    else:
        # page hit -> move it to end (most recently used)
        memory.remove(page)
        memory.append(page)
    
    print(f"Step {i+1}: Page={page} | Memory={memory}")

print("\nTotal Page Faults:", faults)