## Multithreading
## When to use multi threading
## I/O bound tasks: tasks that spend more time
## wating for I/O operations (e.g., file operations
# network requests)

##concurrent execution: when you want to improve the throughput
## of your application by performing multiple operations concurrently

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"number:{i}")
        
def print_letters():
   
    for letter in "abcde":
        time.sleep(2)
        print(f"letters: {letter}")
        
##create 2 threads
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_letters)
        
t = time.time()
        
#start the thread
t1.start()
t2.start()

#wait for the threads to complete
t1.join()
t2.join()

finished_time = time.time() - t

print(finished_time)

        
