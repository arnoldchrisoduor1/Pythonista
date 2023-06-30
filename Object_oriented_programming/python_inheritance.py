#derived calss or child class inherits from the parent,
#or the base class.
print()
print("Inheritance in action")

class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)

p1 = Person("Joel", "Austin")
print("This is the parent class: ")
p1.printname()
print()

class student(Person):
    pass

x = student("Arnold", "chris")
print("This is the child / derived class: ")
x.printname()

#Adding separate __init__() functions to the class.
print()
print("Adding a separate child __init()__ function.")

class Cat():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)

class kitten(Cat):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.born = year

    def welcome(self):
        print("Today we welcome ",self.firstname, self.lastname, " to the family, K was born in " ,self.born)

k = kitten("Jucinta", "adhoch", 2005)
k.welcome()
print()
        
