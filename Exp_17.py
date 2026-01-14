
# Deadlock Prevention using Resource Ordering
import threading
import time


# Resources
R1 = threading.Lock()
R2 = threading.Lock()

  
# Process 1
def process1():
    print("P1 requesting R1")
    with R1:
        print("P1 acquired R1")
        time.sleep(1)
        print("P1 requesting R2")


        with R2:
           print("P1 acquired R2")
           print("P1 executing critical section")



# Process 2
def process2():
    print("P2 requesting R1")
    with R1:
        print("P2 acquired R1")
        time.sleep(1)
        print("P2 requesting R2")


        with R2:
           print("P2 acquired R2")
           print("P2 executing critical section")


# Create threads
t1 = threading.Thread(target=process1)
t2 = threading.Thread(target=process2)


# Start threads
t1.start()
t2.start()


# Wait for completion
t1.join()
t2.join()
print("No Deadlock Occurred!")






