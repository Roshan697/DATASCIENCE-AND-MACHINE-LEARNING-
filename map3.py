#multiple iterables

numbers1 = [1,2,3]
numbers2 = [4,5,6]

add_num = list(map(lambda x,y:x+y,numbers1,numbers2))

print(add_num)