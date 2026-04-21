## FILTER WITH LAMBDA FUNCTION AND MULTIPLE CONDITIONS


lst = [1,2,3,4,5,6,7,8,9,10,11,12]
even_and_greater_than_five = list(filter(lambda x:x>5 and x%2 ==0,lst))

print(even_and_greater_than_five)
