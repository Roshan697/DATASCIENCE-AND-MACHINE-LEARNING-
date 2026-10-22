import logging

logging.basicConfig(
    filename = "app4.log",
    filemode= "w",
    level = logging.INFO,
    
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt= '%Y-%m-%d %H-%M-%S'
)
# logger 1
login_logger = logging.getLogger("login")

# logger 2 
payment_logger = logging.getLogger("payment")

login_logger.info("User logged in")
payment_logger.info("Payment successful")


