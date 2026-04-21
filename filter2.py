'''def even(num):
    if num%2==0:
        return True
    
lst = [1,2,3,4,5,6,7,8,9,10,11,12]

print(list(filter(even,lst)))'''

#filter with a lambda function

number = [1,2,3,4,5,6,7,8]

lst = [1,2,3,4,5,6,7,8,9,10,11,12]


greater_than_five = list(filter(lambda x:x>5,lst))
print(greater_than_five)