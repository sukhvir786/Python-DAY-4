"""
    Program to add the sum of the digits
    in any range
    may be from 12 to 93
    from 34 to 57, from 15 to 27, from 1 to 100
    etc...
"""
s1 = 0
for i1 in range(12,94):
    s1 = s1 + i1 
print("Sum (12 to 93) : ",s1)

s2 = 0
for i2 in range(34,58):
    s2 = s2 + i2 
print("Sum (34 to 57) : ",s2)

s3 = 0
for i3 in range(15,28):
    s3 = s3 + i3 
print("Sum (15 to 27) : ",s3)

s4 = 0
for i4 in range(1,101):
    s4 = s4 + i4 
print("Sum (1 to 100) : ",s4)