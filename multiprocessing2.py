import multiprocessing 
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"square : {i*i}")
        
def cube_nummbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube: {i*i*i}")