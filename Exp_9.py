# Page Replacement Algorithms: FIFO and LRU

# Input: list of pages and frame size
pages = [1, 3, 0, 3, 5, 6, 3]
capacity = 3

print("Pages:", pages)
print("Frame size:", capacity)
print("\n--- FIFO Page Replacement ---")

# ---------- FIFO (First In First Out) ----------
memory = []        # to store pages in memory
faults = 0         # count of page faults

for page in pages:
    # if page not in memory -> page fault occurs
    if page not in memory:
        faults += 1
        # if memory is full, remove the oldest page (first inserted)
        if len(memory) == capacity:
            memory.pop(0)
        # add the new page
        memory.append(page)
    # print the current state of memory
    print(f"Page: {page} -> Memory: {memory}")

print("Total Page Faults (FIFO):", faults)


# ---------- LRU (Least Recently Used) ----------
print("\n--- LRU Page Replacement ---")

memory = []        # reset memory for LRU
faults = 0

for page in pages:
    # if page not in memory -> page fault
    if page not in memory:
        faults += 1
        # if memory full, remove least recently used (first in list)
        if len(memory) == capacity:
            memory.pop(0)
        # add the new page
        memory.append(page)
    else:
        # if page already in memory -> move it to end (most recently used)
        memory.remove(page)
        memory.append(page)
    # print current state of memory
    print(f"Page: {page} -> Memory: {memory}")

print("Total Page Faults (LRU):", faults)
