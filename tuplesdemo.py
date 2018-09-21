"""
 Tuple
 Like list but they are imutable
 It means you can't change them
"""

my_list=[1,2,3]

print(my_list)

"""
 output

 [1,2,3]

"""

my_list[0]=0
print(my_list)

my_tuple=(1,2,3,4,2,4,2,4,3,4,4)
print(my_tuple)

print("*#"*20)

#my_tuple[0]=0
#print(my_tuple)

"""
 output

   my_tuple[0]=0
TypeError: 'tuple' object does not support item assignment

"""
print(my_tuple[0])

print(my_tuple[1:])

####output######
"""
 *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
1
(2, 3)

"""

print(my_tuple.index(2))

print(my_tuple.count(1))

print(my_tuple.count(3))

print(my_tuple.count(4))
####output####
"""
1
1
2
5
"""
