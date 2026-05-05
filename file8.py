import os
##checking if the path is file or directory

path = 'example.txt'
if os.path.isfile(path):
    print("this path is a file")

elif os.path.isdir(path):
    print("this path is a directory")
    
else:
    print("neither a file nor a directory")