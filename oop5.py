class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p1 = Person()
p2 = Person()

p1.name = "Emily"
p2.age = 36

print(p1.name)
print(p2.age)