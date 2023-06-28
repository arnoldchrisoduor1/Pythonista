#adding items to the list.
print("Adding items to the list")
x = ("apples", 2, "three", "mangoes")
print("Before", x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print("After : ",x)

#appending to a tuple
print("\n")
print("appending to a tuple")
thistuple = ("night", "day", "evening","daylight")
print("Before : ",thistuple)
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print("After : ",thistuple)

#adding to tuples
print("\n")
print("Adding two tuples")
ntuple = ("This", "that", "these")
y = (2, 5)

ntuple += y
print(ntuple)

#unpacking a tuple
print("\n")
print("unpackig a tuple")
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#unpacking tuple using asterick
print("\n")
print("Unpacking using an asterick")
(apples, *nest) = thistuple
print(apples)
print(nest)

#multiple contents in a tuple
print("\n")
print("Multiplying items in a tuple")
mtuple = ("apples", "bible", "great")
gres = mtuple * 2
print(gres)