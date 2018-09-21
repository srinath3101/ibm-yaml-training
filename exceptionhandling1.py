"""
Exceptions are errors
We should handle exception in our code
to make sure that code is working the way we want and is handling all the unwanted issues
Link to 3.5 built-in exception- https://docs.python.org/3/libray/exceptions.html"""

def exceptionHandling():
    try:
        a=10
        b="any string"
        c=10

        d=(a+b)/c
        print(d)
    except:
         print("In the except block, this is not possible")

exceptionHandling()
