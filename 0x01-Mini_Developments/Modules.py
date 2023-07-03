#Creating an alias when importing a module.
import mymodule as mx

print()
a = mx.person1["age"]
print(a)

#The dir() function to name all functions in a,
#module.
print()
import platform

x = dir(platform)
print(x)

#We can import a single entity through:
#from mymodule import person1

#Then we can use x = person["age"] instead.