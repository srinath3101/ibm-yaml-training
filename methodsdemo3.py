"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from outside
"""

def sum_nums(n1=2,n2=4):

    return n1+n2

sum1= sum_nums(2,8)
print(sum1)

"""
 output: 10

"""
print("***************************")

sum1=sum_nums()
print(sum1)

"""
 *********output********
6
"""

print("*****************************")

sum1=sum_nums(n1=8)
print(sum1)

"""
  output
******************
12

"""
