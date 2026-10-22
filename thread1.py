import threading

def task1():
    print("task 1 is running")
    
def task2():
    print("task 2 is running")
    
t1 = threading.Thread(target = task1)

t2 = threading.Thread(target = task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("main program has finished")

