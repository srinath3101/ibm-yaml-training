"""
 Inheritance
"""

class Car(object):
    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started....")
   
    def stop(self):
        print("Car stopped")

#c=Car()

#c.drive()
#c.stop()

"""
 ***output****
You just created the car instance
Car started....
Car stopped
"""
class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("You just create the BMW instance")


c=Car()
c.drive()
c.stop()

b= BMW()
b.drive()
b.stop()

"""
 *****output****
You just created the car instance
Car started....
Car stopped
You just created the car instance
You just create the BMW instance
Car started....
Car stopped
"""


