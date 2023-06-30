#iterator is a python object which impliments the,
#iterator methods __iter__() and __next()__

#An iterator is an object that can be iterated upon.

print()
#Getting an iterator from a tuple.
print("Getting an itertaor from a tuple")
mytuple = ("mangoes", "carrots", "oranges")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print()

#The for loop actually creates an iterator object and, 
#executes the next() method for each loop.

#Creating an iterator the returns the numbers 1 through 5.
print("Iterator that returns numbers 1 -- 5")

class MyNumbers():
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))

#or

for x in myiter:
    print(x)