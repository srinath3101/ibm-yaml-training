"""

Examples to show available string method in python

"""

#Replace methods

a="1abc2abc3abc4abc"

print(a.replace('abc','ABC'))

#output

"""
1ABC2ABC3ABC4ABC

"""

print(a.replace('abc','ABC',1))

###output

"""

1ABC2abc3abc4abc

"""

#Sub-strings

#starting index is inclusive

#Ending index is exclusive

sub=a[1]

print("*********************")

sub=a[1:6]

step=a[1:6:1]

print (sub)

print(step)

###output

"""

abc2a
abc2a

"""

step1= a[1:6:2]

print(step1)

####output

"""
aca

"""

step2=a[1:6:3]

print(step2)

###output

"""
a2

"""
