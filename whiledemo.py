"""
 Execute statements repeatedly
 Conditions are used to stop the execution of loops
 Iterable items are Strings, list, Tuple,Dictionary
"""
x=0
while x<10:
    print("Value of x is:" + str(x))
    x=x + 1
"""
 output
Value of x is:0
Value of x is:1
Value of x is:2
Value of x is:3
Value of x is:4
Value of x is:5
Value of x is:6
Value of x is:7
Value of x is:8
Value of x is:9
"""

l=[]
num=0
while num<10:
    l.append(num)
    print("Value of num is:" +str(num))
    num+=1
print(l)

######*******************########
"""
Value of num is:0
Value of num is:1
Value of num is:2
Value of num is:3
Value of num is:4
Value of num is:5
Value of num is:6
Value of num is:7
Value of num is:8
Value of num is:9
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


