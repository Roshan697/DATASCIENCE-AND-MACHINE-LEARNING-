##file handling and exception handling

try:
    
    file = open('example3.txt','r')
    content = file.read()
    print(content)
    
except FileNotFoundError:
    print("the file does not exists")
    
except Exception as ex:
    print(ex)
    
finally:
    if file in locals() or file.closed():
        file.close()
        print("file closed")
    