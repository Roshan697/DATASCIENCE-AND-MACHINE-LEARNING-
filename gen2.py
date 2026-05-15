def my_gene():
    yield 1
    yield 2
    yield 3
    
gen = my_gene()
print(gen)
print(next(gen))
print(next(gen))

for val in gen:
    print(val)
