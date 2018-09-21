"""
  Data type to store more than one value in one variable name
  List items are in brackets, seperated with "," [1,2,3]
"""

cars= ["bmw","audi","honda"]

empty_list=[]
print(cars)
print(empty_list)

print("*#"*20)

print(cars[1])

num_list= [1,2,3]

sum_num= num_list[0] + num_list[1]

print(sum_num)

more_cars= ["bmw","honda","audi"]
print(more_cars[1])

more_cars[1]="benz"

print(more_cars[1])

print(more_cars)

###output ###

"""
['bmw', 'audi', 'honda']
[]
*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
audi
3
honda
benz
['bmw', 'benz', 'audi']

"""
