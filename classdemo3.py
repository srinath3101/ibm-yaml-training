"""
 Object Oriented Programming
 Create Your Own Methods
"""

class Car(object):
  
    wheels = 4
 
    def __init__(self,make,model):
        self.make=make
        self.model=model

    def info(self):
        print "Make of the car:" , self.make
        print "Model of the car:", self.model

print(Car.wheels)
c1=Car('bmw','550i')
print(c1.make)
#print(c1.wheels)
#c1.info()

c2=Car('benz','E350')
print(c2.make)
#print(c2.wheels)
#c2.info()

print(Car.wheels)
"""
 ****output****

here we call c1.info() and c2.info()

Make of the car: bmw
Model of the car: 550i
Make of the car: benz
Model of the car: E350
"""

"""
4
bmw
benz
4
""" 
