"""
  Built-in methods to help manipulating a list
"""

cars= ["bmw","honda","audi"]

length=len(cars)

print(length)

cars.append("benz")

print(cars)

####output######
"""
3
['bmw', 'honda', 'audi', 'benz']

"""

cars.insert(1,"Jeep")
print(cars)

####output ####

"""
['bmw', 'Jeep', 'honda', 'audi', 'benz']
"""

x=cars.index("honda")
print(x)

###output ####
"""
2
"""

###remove item from the list ######

y=cars.pop()

print(y)
print(cars)

"""
benz
['bmw', 'Jeep', 'honda', 'audi']
"""

cars.remove("Jeep")

print(cars)

###output ####

"""
['bmw', 'Jeep', 'honda', 'audi']
['bmw', 'honda', 'audi']
"""
### Slicing from a list ######

slicing= cars[0:2]

print(slicing)

###output ###

"""
['bmw', 'honda', 'audi']
['bmw', 'honda']

"""
a = cars[1:]
print(slicing)
print(a)

###output####

"""
['honda', 'audi']

"""
print("*#"*20)
print(cars)

cars.sort()

print(cars)

###output #####

"""
['bmw', 'honda', 'audi']
['audi', 'bmw', 'honda']

"""
