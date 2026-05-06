## try,except and else block

try:
    num = int(input("enter a number: "))
    result = 10/num
    
except ValueError:
    print("not valid number")
    
except ZeroDivisionError:
    print("you cannot divide by zero")
    
except Exception as ex:
    print(ex)
    
else:
    print(f"the result is {result}")
    