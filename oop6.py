## you can set default values in __init__() method

class Person():
    def __init__(self,name, age = 22):
        self.name = name 
        self.age = age
        
p1 = Person("Emil")
p2 = Person("Tobias",25)

print(p1.name,p1.age)
print(p2.name,p2.age)