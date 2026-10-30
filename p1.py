import time
def print_numbers(n):
    
    for i in n:
        time.sleep(3)
        print(f"numbers: {i}")

n = [1,2,3,4,5]
print_numbers(n)