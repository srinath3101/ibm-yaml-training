"""
  and
  *******************************
  True and True ---> True
  True and False --> False
  Falase and False --> False

  or
  ********************************
  True or True  --> True
  True or False --> True
  False or False --> False

  not
  ********************************
  Not True --> False
  Not False --> True
"""
and_output1=(10==10) and (10 > 9)
and_output2=(10==10) and (10 < 9)
and_output3=(10 > 10) and (10 < 9)

print(and_output1)
print(and_output2)
print(and_output3)

###**********output*****#####
"""
 True
 False
 False
"""
or_output1=(10==10) or (10 > 9)
or_output2=(10==10) or (10 < 9)
or_output3=(10>10) or (10 < 9)

print "First or output is :" ,or_output1
print "Second or output is :",or_output2
print "Third or output is :",or_output3

"""
First or output is : True
Second or output is : True
Third or output is : False
"""
not_true= not(10==10)

print(not_true)
"""
 False
"""
not_false= not(10 < 9)

print(not_false)

"""
True
"""
