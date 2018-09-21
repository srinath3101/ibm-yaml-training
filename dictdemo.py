"""
  Data type to store more than one value in one variable name , in terms of
  key value pairs
  Dictionary items are in brackets {} in key:value pairs, seperated with ","
  {'k1':'v1','k2':'v2'}
  Not sequenced(no particular order), no indexing -> Mapping
"""

car = {'make':'bmw','model':'555i','year': 2016}
print(car)

###output ####
"""
{'make': 'bmw', 'model': '555i', 'year': 2016}

"""
print(car['make'])

print(car['model'])

print(car['year'])

###output###

"""
bmw
555i
2016

"""
d={}

model = car['model']

print(model)

print(d)

####output ####
"""
555i

{}

"""

print("*#"*20)

d['one']=1
d['two']=2

print(d)

"""
{'two': 2, 'one': 1}

"""

sum_1=d['two'] + 8

print(sum_1)

###output ####
"""
10 

"""
###***************************#####
print(d)

d['two']= d['two'] + 8

print(d) 

##*****************************#####
###output ###########
"""
{'two': 2, 'one': 1}
{'two': 10, 'one': 1}

"""
