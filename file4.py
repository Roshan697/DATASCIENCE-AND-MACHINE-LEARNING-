##writing and then reading a file 

with open('example3.txt','w+') as file:
    content =  file.write('this is a new file\n')
    file.write('updating on github')
    
    ##Move the file cursor to the beginning
    
    file.seek(0)
    
    ##read the content of the file
    content = file.read()
    print(content)
    