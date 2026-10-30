import time
from concurrent.futures import ThreadPoolExecutor

def print_numbers(n):
    time.sleep(2)
    return f"Number: {n}"

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers,[1,2,3,4,5])
    
    for result in results:
        print(result)
        
print("all tasks completed")