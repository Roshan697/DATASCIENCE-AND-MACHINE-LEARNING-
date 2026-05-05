## listing files and directories 
import os
'''items = os.listdir('.')
print(items)'''

##joining paths
dir_name = "package2"

file_name = "example2.txt"

full_path = os.path.join(dir_name,file_name)
print(full_path)
