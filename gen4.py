def greeting_generator():
    print("generator started ")
    
    while True:
        name = yield "Ready for name..."
        yield f"hello, {name}!"
        
gen = greeting_generator()
print(next(gen))
print(gen.send("Alice"))

print(next(gen))
gen.close()