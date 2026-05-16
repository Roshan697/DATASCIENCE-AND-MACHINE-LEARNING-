def simp():
    yield "first"
    yield "second"
    yield "third"

gen = simp()

print(next(gen))
print(next(gen))
