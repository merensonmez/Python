""""'
text type = str
numeric types = int,float,complex
sequence types = list,tuple,range
mapping type = dict
set types = set,frozenset
boolean type = bool
binary types = bytes,bytearray,memoryview
none type = NoneType
"""
'''x = 5 
print(type(x))'''

x = 1 #int
y = 2.8 #float
z = 1j #complex

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(x))
print(type(y))
print(type(z))


# Random Number
import random
print(random.randrange(1, 10))

