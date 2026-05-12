class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        
    def celebrate(self):
        self.age += 1
        print(f"happy birthday! you are now {self.age}")
        
p1 = Person("Linus",25)
p1.celebrate()