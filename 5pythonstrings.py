#Slicing strings

'''b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])
'''

''#UpperCase
a = "Hello, World!"
print(a.upper())

#LowerCase
a = "Hello, World!"
print(a.lower())

#Remove Whitespace
a = " Hello, World! "
print(a.strip())

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
a = "Hello, World!"
print(a.split(","))

#String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String Format
age = 19
txt = f"My name is Eren, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

