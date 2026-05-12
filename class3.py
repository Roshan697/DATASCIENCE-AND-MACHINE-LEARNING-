class Person:
    lastname = ""
    
    def __init__(self,name):
        self.name = name
   
     
p1=Person("Linus")
p2=Person("Emil")

Person.lastname = "Refsenes"

print(p1.lastname)
print(p2.lastname)
        