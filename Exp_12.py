# 12 implement Optimal Page Replacement algorithm

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3] # Page reference string
capacity = 3 # Number of frames
frames = [] # Memory frames
page_faults = 0


for i in range(len(pages)):
    page = pages[i]

    # If page is already in frames → no fault
    if page in frames:
       print(f"{page} → Hit")
       continue


    # Page Fault occurs
    page_faults += 1



    # If empty space available → add page
    if len(frames) < capacity:
          frames.append(page)
          print(f"{page} → Page Fault (Added)")


    else:
        # Find the page to replace using Optimal rule
        future = pages[i+1:]
        index_list = []



        for f in frames:

            if f in future:
                index_list.append(future.index(f))

            else:
                 index_list.append(9999) # Never used again → highest priority to replace


        # Replace the page with farthest future use
        replace_index = index_list.index(max(index_list))
        print(f"{page} → Replace {frames[replace_index]}")
        frames[replace_index] = page

print("\nTotal Page Faults =", page_faults)









