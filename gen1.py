def square(n):
    for i in range(n):
        yield i**2
    
print(square(3))

for i in square(3):
    print(i)
    
a = square(3)
print(next(a))
print(next(a))

        