#Arbitrary arguements (Args) in python
print("\n")
print("Args in functions")
def children(*kids):
    print("The children are " + kids[2])

children("Emily", "Greta", "Johnson", "Mary")

#arguements as key value pairs.
print("\n")
print("Functions as key value pairs.")
def child(child1, child2, child3):
    print("Child three's name is "+ child3)
    print("Parent of " + child2 + " is unknown")

child(child1 = "Ken", child2="kevin", child3="arnold")

#Keyword arguements in python (Kwargs)
print("\n")
print("Keyword arguements in Functions")
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
print("\n")

#Default parameter value
print("Creating the default parameter value")
print()
def area(counry = "Norway"):
   print("I come from " + counry)

area("Kenya")
area("Sweden")
area()
area("Netherlands")
print()

#passing a list as an arguement
print("Passing a list as an arguement")
def food(foo):
   for x in foo:
      print(x)

fruits = ["cherry", "apples", "oranges", "bananaa"]
food(fruits)
print()

#The pass statement can be used to create an empty function.

#Recusrion
print("Recursion")
def recur(k):
   if k > 0:
      num = k + recur(k-1)
      print(num)
   else:
      num = 0
    
   return num

recur(7)