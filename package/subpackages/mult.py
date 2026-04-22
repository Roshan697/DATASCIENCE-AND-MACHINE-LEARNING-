def multiply():
    
    count = int(input("How many numbers you want to multiply"))
    result = 1
    for i in range(count):
        num = float(input(f"Enter number {i + 1}: "))
        result *= num
    print("the result is : ",result)
    
    
