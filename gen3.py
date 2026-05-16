# Reading large files

def read_large_file(file_path):
    with open(file_path,'r') as f:
        for line in f:
            yield line
            
            
file_path = 'large_file.txt'

for line in read_large_file(file_path):
    print(line.strip())