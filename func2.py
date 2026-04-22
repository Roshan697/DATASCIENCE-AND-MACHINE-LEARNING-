def add_pair(a,b=None):
    if b is None:
        
        b = {} #create an empty dictionary
    
    b[a] = 1 #add a key value pair
    return b

print(add_pair(2))
print(add_pair("b",{"a":1}))