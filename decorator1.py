def decorator(func):
    
    def wrapper():
        print("before function")
        
        func()
        
        print("after function")
        
    return wrapper

def hello():
    print("hello")
    
hello = decorator(hello)

hello()