#Variables
x = 5 
y = "Hello,World!"

'''print(x)
print(y)'''

'''x = str(3) #String '3'
y = int(3) #Integer 3
z = float(3) #Float 3.0

myVariableName = "John"
print(myVariableName)
'''

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)    

x = 5
y = 10
print(x + y)

#Global Variables
x = "awesome"

def myfunc():
    print("Python is "+x)

myfunc()

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

carname = "Volvo"
print(carname)