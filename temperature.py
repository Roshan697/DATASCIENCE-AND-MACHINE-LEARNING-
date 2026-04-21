def temperature(temp,unit):
    """this function converts temperature to 
    celcius and fahrenhiet"""
    
    if unit == 'C':
        return temp * 9/5 +32 ##celcius to fahrenhiet
    
    elif unit == "F":
        return (temp-32)*5/9 ##fahrenhiet to celcius
    
    else:
        return None
    
    
print(temperature(25,'C'))

print(temperature(77,'F'))     