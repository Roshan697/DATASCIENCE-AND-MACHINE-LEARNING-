try:
    num = int(input("enter a number: "))
    result = 10 / num
    print(result)
    
except ValueError:
    print("this is not a valid number")
    
except ZeroDivisionError:
    print("enter denominator greater than 0")
    
except Exception as ex:
    print(ex)
    