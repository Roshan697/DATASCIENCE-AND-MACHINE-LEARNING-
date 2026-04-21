## map() :- applies a function to all items in a list
numbers = [1,2,3,4,5,6]
def square(numbers):
     return numbers**2

square(2)

print(list(map(lambda x: x**2,numbers)))
