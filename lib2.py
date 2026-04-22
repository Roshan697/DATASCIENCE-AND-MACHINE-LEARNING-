##file and directory access

import os 
print(os.getcwd()) 
##os.mkdir('test_dir')

##high level operations on files and collections of files

import shutil
shutil.copyfile('source.txt','destination.txt')  