import os

path = 'example1.txt'
if os.path.exists(path):
    print(f"this specific path {path} exists")
    
else:
    print(f"this particular {path} does not exists")
    

    