class Person:
    species = "Human" #class property
    
    def __init__(self,name):
        self.name = name
        
p1= Person('emil')
p2 = Person('Tobias')

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)        