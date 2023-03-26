
# When we create a class we can inherit all of the fields and methods
# from another class. This is called inheritance.

# The class that inherits is called the subclass and the class we
# inherit from is the super class

# This will be our super class
class Animal:

    def __init__(self, birthType="Unknown",
                 appearance="Unknown",
                 blooded="Unknown"):
        self.__birthType = birthType
        self.__appearance = appearance
        self.__blooded = blooded

    # The getter method
    @property
    def birthType(self):
        # When using getters and setters don't forget the __
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    # Can be used to cast our object as a string
    # type(self).__name__ returns the class name
    def __str__(self):
        return "A {} is {} it is {} it is " \
               "{}".format(type(self).__name__,
                           self.birthType,
                           self.appearance,
                           self.blooded)

# Create a Mammal class that inherits from Animal
# You can inherit from multiple classes by separating
# the classes with a comma in the parentheses

# inheritance
class Mammal(Animal):
    def __init__(self, birthType="born alive",
                 appearance="hair or fur",
                 blooded="warm blooded",
                 nurseYoung=True):
        # Call for the super class to initialize fields
        Animal.__init__(self, birthType,
                        appearance,
                        blooded)

        self.__nurseYoung = nurseYoung

    # We can extend the subclasses
    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def appearance(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    # Overwrite __str__
    # You can use super() to refer to the superclass
    def __str__(self):
        return super().__str__() + " and it is {} they nurse " \
                                   "their young".format(self.nurseYoung)


class Reptile(Animal):
    def __init__(self, birthType="born in an egg or born alive",
                 appearance="dry scales",
                 blooded="cold blooded"):
        # Call for the super class to initialize fields
        Animal.__init__(self, birthType,
                        appearance,
                        blooded)

    # Operator overloading isn't necessary in Python because
    # Python allows you to enter unknown numbers of values
    # Always make sure self is the first attribute in your
    # class methods
    def sumAll(self, *args):
        sum = 0

        for i in args:
            sum += i

        return sum


def main():
    animal1 = Animal("Is warm blooded")
    print(animal1.blooded)
    print(animal1)

    print()
    mammal1 = Mammal()
    print(mammal1.appearance)
    print(mammal1.blooded)
    print(mammal1.birthType)
    print(mammal1.nurseYoung)

main()
