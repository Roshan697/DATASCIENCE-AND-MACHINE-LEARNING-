## BINARY FILES

## Writing to a binary file

data = b'\x00\x01\x02\x03\x04'

with open('bina.bin','wb') as file:
    file.write(data)

## read a content from a source text file and write it to a destination text file 


with open('example.txt',) as file:
    content = file.read()
    
with open('destination.txt','w') as file:
    file.write(content) 
    
    
