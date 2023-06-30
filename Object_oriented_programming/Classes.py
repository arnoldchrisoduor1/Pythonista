#classes are basically blueprints for objects.
print()
class Nclass():
    x = 5

p1 = Nclass()
print(p1.x)
print()

#using the init function
print("Using the init function")
class Person():
    def __init__(self, name, age):
        Person.name= name
        Person.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print()

#Using the __str__() function.
print("Using te=he __str__() function")
class Dog():
    def __init__(self, breed, age):
        Dog.breed = breed
        Dog.age = age

    def __str__(self):
        return f"{self.breed} {self.age}"
    
d1 = Dog("shelby", 7)
print(d1)
print()

#Creating object methods.
print("Creating object Methods")
class student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("The student's name is " + self.name)

s1 = student("Greta", 9)
s1.myfunc()
print()

#Modify object properties through
#p1.name = "Julia"

#delete object properties through the command.
#del p1.age

#delete objects through.
#del p1

#A class with no content is done by:
#class Newclass():
#   pass