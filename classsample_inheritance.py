class Fruit(object):

    def __init__(self):
        print("First statement")
    def nutrition(self):
        print("Good for health")
    def fruit_shape(self):
        print("Fruit shape owel")

class Mango(Fruit):
     
    def __init__(self):
        Fruit.__init__(self)
        print("I am Mango")
    def nutrition(self):
        print("Mango nutrition")
    def color(self):
        print("Color is orange")

F=Fruit()

F.nutrition()
F.fruit_shape()

M=Mango()

M.nutrition()
M.fruit_shape()
M.color()

"""
 ***exercise output***
First statement
Good for health
Fruit shape owel
First statement
I am Mango
Mango nutrition
Fruit shape owel
Color is orange
"""      
