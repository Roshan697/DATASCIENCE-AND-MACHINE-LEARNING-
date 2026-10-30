import threading 
import time 

def task():
    time.sleep(3)
    print("task completed")
    
t1 = threading.Thread(target = task)
t1.start()
t1.join()

print("Main program completed")
