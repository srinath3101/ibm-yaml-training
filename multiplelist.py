"""
 Iterating multiple lists at the same time-using the zip function
"""
import itertools
l1=[1,2,3]
l2=[6,7,8,20,30,40]

for a,b in zip(11,12):
    print(a)
    print(b)

"""
 ********output******

1
6
2
7
3
8

here we are matching the pair, after 3 pair is not matching

that's why it display only matching pair

"""

