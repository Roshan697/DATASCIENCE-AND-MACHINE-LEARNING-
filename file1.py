##read a whole file

with open('example1.txt','r') as file:
    content = file.read()
    print(content)


##read a file line by line

with open('example1.txt','r') as f:
    for line in f:
        print(line.strip()) ##.strip() character removes the newllien character


##writing in file operations 
with open('example1.txt','w') as file:
    file.write("Hell nahhh!!!")
    file.write('this is a new line')    

##writing in file without overwriting the existing content

with open('example1.txt','a') as file:
    file.write("append operation taking place \n")
    
## writing list of lines to a file

lines = ['first line \n', 'second line\n','third line \n']

with open('example1.txt','a') as file:
    file.writelines(lines)



