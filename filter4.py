# filter to check if the age is greater than 25 in dictionaries

people = [{'name':'krish','age':32},
          {'name':'Jack','age':33}]

def age(person){
    
    return person['age']>25
}

list(filter(age,people))