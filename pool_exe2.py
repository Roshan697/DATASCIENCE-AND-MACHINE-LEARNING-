## using map(best for applying the sam task 
# for multiple items)

import time
from concurrent.futures import ThreadPoolExecutor

def fetch_data(site_id):
    print(f"starting download for site {site_id}")
    time.sleep(2) # simulating the network delay
    return f"data from site {site_id}"

site = [1,2,3,4,5]

# using a context manager ensures threads are 
#cleaned up automatically

with ThreadPoolExecutor(max_workers = 3) as executor:
    #map runs fetch_data concurrently for each site ID
    results = executor.map(fetch_data,site)
    
#print results (returned in order)
for result in results:
    print(result)