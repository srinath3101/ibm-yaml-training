"""
 Built-in function
 Create a sequence of numbers but does not save them in memory-python 3
 Very useful for generating numbers
"""
print(range(0,10))

"""
 *****output****
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""

a= range(12,100)
print(a)
print(type(a))

"""
 ***output***
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
<type 'list'>

"""
b= range(10,20,2)
print(b)

###output#####
"""
[10, 12, 14, 16, 18]
"""
l=[1,2,3]

for num in range(1,4):
    print(num)

""" 
 **********output***********
1
2
3
"""
