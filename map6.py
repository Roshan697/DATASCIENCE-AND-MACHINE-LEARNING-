def get_name(person):
    return person['name']

people = [{'name':'krish','age':32},
          {'name':'Jack','age':33}]

list(map(get_name,people))
print(list(map(get_name,people)))
