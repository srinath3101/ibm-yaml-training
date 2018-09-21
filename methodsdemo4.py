"""
Variable Scope
"""

a=10

def test_method(a):
    print "Value of local a is:" , a
    a=2
    print "New value of local a is", a
print "Value of global a is:",a

test_method(a)

print "Did the value of global a change?" , a

"""
 ***********output*********
Value of global a is: 10
Value of local a is: 10
New value of local a is 2
Did the value of global a change? 10
"""

print("*******************************")

def test_method1():
    global a
    print "Value of 'a' inside the method is:" ,a
    a=2
    print "New value of 'a' inside the methode is changed to :" ,a
  
print "Value of global a is:" ,a

test_method1()
print "Did the value of global 'a' change?" , a

"""
 ***output***
Value of global a is: 10
Value of 'a' inside the method is: 10
New value of 'a' inside the methode is changed to : 2
Did the value of global 'a' change? 2
"""

