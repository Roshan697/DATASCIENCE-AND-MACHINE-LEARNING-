import logging

## loggin configuration

logging.basicConfig(
  
    filemode="w"
    level = logging.DEBUG
    format='%(astime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    handlers=[
        logging.FileHandler("app4.log"),
        logging.StreamHandler()
        
    ]
    
)

logger = logging.getlogger("ArithmeticApp")

def add(a,b):
    result = a+b 
    logger.debug(f"Adding {a} + {b} = ",result)
    return result

def subtract(a,b):
    result = a - b
    logger.debug(f"subtracting {a} * {b} = ",result)
    return result

def multiply(a,b):
    result = a * b
    logger.debug(f"Multiplying {a}*{b} = ",result)
        
def divide(a,b):
    if(b == 0):
        logger.debug("division by 0 is not allowed.")
        return None
    
    else:
        return a/b
    
    
    
