"""
  Dictionary Methods
"""
car = {'make':'bmw','model':'550i','year':2016}

cars = {'bmw': {'model':'550i','year':2016},'benz': {'model':'E350','year':2015}}

print(car.keys())
print(cars.keys())
####**********output*******####
"""
['make', 'model', 'year']
['benz', 'bmw']
"""
print("*#"*20)

print(car.values())
print(cars.values())

"""
  output

*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
dict_keys['bmw', '550i', 2016]
dict_values[{'model': 'E350', 'year': 2015}, {'model': '550i', 'year': 2016}]

"""
print(car.items())

###output######
"""
 [('make', 'bmw'), ('model', '550i'), ('year', 2016)]

"""

####copy a dictionary #####

car_copy= car.copy()

print(car_copy)

####output#####

"""
 {'make': 'bmw', 'model': '550i', 'year': 2016}

"""

####Clear the dictionary ######

#car.clear()


###pop the keys ####

print(car)

print("*#"*20)

print(car.pop('model'))

print(car)

"""
 {'make': 'bmw', 'model': '550i', 'year': 2016}
  
  *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
  550i
 {'make': 'bmw', 'year': 2016}

"""



