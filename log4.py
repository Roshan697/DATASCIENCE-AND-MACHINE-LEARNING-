import logging 

logging.basicConfig(
    filename="app.log",
    level = logging.INFO
)

username = input("Enter username: ")
password = input("Enter password: ")

if username == "roshan" and password == "1234":
    print("login sucessfull")
    logging.info("User logged in successfully")
    
else:
    print("Invalid username or password")
    logging.warning("Failed login attempt")