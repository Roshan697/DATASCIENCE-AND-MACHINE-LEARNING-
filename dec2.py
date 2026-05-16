def greet(fx):
    def mfx(*args,**kwargs):
       print("Good mornin")
       fx(*args,**kwargs)  # hello 
       print("thanks for using this function ")
    return mfx

@greet
def hel():
    print("helo")




#@greet
def add(a,b):
    return(a+b)    
hel()

add(1,3)

