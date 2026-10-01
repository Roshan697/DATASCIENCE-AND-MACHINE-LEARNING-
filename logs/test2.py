from logger import logging

def add(a,b):
    
    logging.debug("The addition operation has taken place")
        
    return a+b

logging.debug("The addition function is called")
add(10,22)

    