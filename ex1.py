## Exeption try, except block

try:
    result = 1/2
    
    
except ZeroDivisionError as ex:
    print(ex)
    print("please enter a number greater than 0 in denominator")
    
except Exception as ex1:
    print(ex1)
    print("main exception got caught here")
    