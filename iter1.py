My_list = [1,2,3,4,5,6]
for i in My_list:
    print(i)
    #print(type(My_list))
    

Iterator = iter(My_list) #list_iterator class 
print (type(Iterator))
print(Iterator)

try:
    next(Iterator)
    print(next(Iterator))
    print(next(Iterator))
    print(next(Iterator))
    print(next(Iterator))
    print(next(Iterator))
    print(next(Iterator))
    print(next(Iterator))
    print(next(Iterator))
    print(next(Iterator))
    
except StopIteration:
    print("there are no elements in the list now")
    