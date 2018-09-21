"""
Break: To break out of the closest enclosing loop
Continue: Go to start of the closest enclosing loop
"""

x=0
while x<10:
    print("Value of x is:" +str(x))
    x=x+1

    if x==8:
        break
    print("This example is awesome")
    print("*"*20)
print("Just broke out of the loop")
"""
  output

Value of x is:0
This example is awesome
********************
Value of x is:1
This example is awesome
********************
Value of x is:2
This example is awesome
********************
Value of x is:3
This example is awesome
********************
Value of x is:4
This example is awesome
********************
Value of x is:5
This example is awesome
********************
Value of x is:6
This example is awesome
********************
Value of x is:7
Just broke out of the loop
"""

print("*" *30)

y=0
while y<10:
    print("Value of y is:" +str(y))
    y=y+1

    if y==8:
        continue
    print("This example is awesome")
    print("*"*20)
print("Just broke out of the loop")

"""
  output
Value of y is:0
This example is awesome
********************
Value of y is:1
This example is awesome
********************
Value of y is:2
This example is awesome
********************
Value of y is:3
This example is awesome
********************
Value of y is:4
This example is awesome
********************
Value of y is:5
This example is awesome
********************
Value of y is:6
This example is awesome
********************
Value of y is:7
Value of y is:8
This example is awesome
********************
Value of y is:9
This example is awesome
********************
Just broke out of the loop
"""
z=0
while z<10:
    print("Value of z is:" +str(z))
    z=z+1

    #if x==8:
     #   break
    print("This example is awesome")
    print("*"*20)
else:
    print("Just broke out of the loop")

#####***********OUTPUT*********###
"""
Value of z is:0
This example is awesome
********************
Value of z is:1
This example is awesome
********************
Value of z is:2
This example is awesome
********************
Value of z is:3
This example is awesome
********************
Value of z is:4
This example is awesome
********************
Value of z is:5
This example is awesome
********************
Value of z is:6
This example is awesome
********************
Value of z is:7
This example is awesome
********************
Value of z is:8
This example is awesome
********************
Value of z is:9
This example is awesome
********************
Just broke out of the loop
"""

