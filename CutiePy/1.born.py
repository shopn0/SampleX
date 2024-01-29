# This is my 2nd entry to the lang of Py
# From childhool interest I entered the the world of programming with this language first in year 2018 when i was just a school student with no idea of computers much.
# Here i am again with my static goal this time to learn and master it.

print("This text has been printed from a python program.\n 26 January, 2024")

"""
Fact:
Py uses interpreter which converts EACH high-level program statement into machine code
"""
#Comparison Operators
print("Comparison Operators:")
s1_mark = 50
s2_mark = 60

a = s1_mark == s2_mark
b = s2_mark != s1_mark

print(a)
print(b)

#Logical Comparison Operators
print("Logical Comparison Operators:")

a= False
b= True
c= True

q = (a and b) or ((b or c)and (b and c))
print("q=",q)

#Bitwise Operators
a = 60
b = 13
c=(a&b)
print("a.",c)
x = a<<2 #left shift with 2 bits shift (for right shift it loses bits per right side)
print("e.", x)

#Assigns
d = 4
d += 3 # here, d = d + 3
print(d)

#Operator Priorities:
#left first