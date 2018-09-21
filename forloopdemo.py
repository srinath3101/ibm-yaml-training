"""
 Execute statements repeatedly
 Conditions are used to stop the execution of loops
 Iterable items are strings, list,tuple , Dictionary
"""
my_string='abcabc'

for c in my_string:
    print c,
   
"""
 By default pythons print() function ends with a newline.
 if we want to print string horizontal we will use  any character/string using ewith end parameter

In python 2.7 here is how you do it
 
we just use print c,

In python 3.x
 
we use print (c, end='')

"""
######output#####
"""
a b c a b c
"""

for x in my_string:
    if x=='a':
        print 'A',
    else:
        print x,
print("\n")

#list for loop
cars=['bmw','benz','honda']
for car in cars:
    print(car)
num=[1,2,3]
for n in num:
   print(n*10)

"""
  output

a b c a b c A b c A b c 

bmw
benz
honda
10
20
30

"""
print("*"*20)
#Dictionary for loop
d={'one': 1, 'two': 2, 'three': 3}
for k in d:
    #print(k)
     print(k+ " " +str(d[k]))
"""
 output
********************
two 2
one 1
three 3
"""
print("*"*20)
for k,v in d.items():
    print(k)
    print(v)

"""
output

three
3
two
2
one
1
"""
