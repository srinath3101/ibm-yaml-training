"""
 Method Overriding
"""
class Car(object):

    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped")

class BMW(Car):
 

    def __init__(self):
        Car.__init__(self)
        print("You just created the BMW instance")

    def drive(self):
      #  super(BMW,self).drive()
        print("You are driving a BMW,Enjoy...")
   
    def headup_display(self):
        print("This is a unique feature")

#c=Car()

#c.drive()
#c.stop()

b=BMW()
b.drive()
b.stop()
b.headup_display()

"""
you just created the car instance
You just created the BMW instance
You are driving a BMW,Enjoy...
Car stopped
This is a unique feature

"""

"""
 ***output*** this when we call define super class
You just created the car instance
You just created the BMW instance
Car started...
You are driving a BMW,Enjoy...
Car stopped
This is a unique feature
"""
