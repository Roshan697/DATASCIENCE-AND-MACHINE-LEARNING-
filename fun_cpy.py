def welcome():
    return "Welcome to advanced python course"

wel = welcome
print(wel())

del welcome
print(wel())
