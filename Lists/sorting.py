#sorting alphanumerically
mylist = ["oranges", "mango", "carrots", "apples"]
print("Alphanumeric sorting")
print("initial : ",mylist)
mylist.sort()
print("after : ",mylist)

#sorting numbers
numlist = [x for x in  range(100) if x > 93]
anlist = [x for x in range(10) if x < 7]
numlist.extend(anlist)
print("\n")
print("Numeric sorting")
print("initial : ",numlist)
numlist.sort()
print("after : ",numlist)

#sorting in decending order
print("\n")
print("arrangin list in decending order")
print("initial : ",mylist)
mylist.sort(reverse=True)
print("after : ",mylist)

#using custom sort function
print("\n")
print("Sorting using custom sort function")
#sorts based on which number is closest to 50.
def myfunc(n):
    return abs(n - 50)

nlist = [30, 60, 89, 48, 78]
print("initial : ",nlist)
nlist.sort(key = myfunc)
print("After : ",nlist)


#sort() function is case sensitive therefore all
#words begining with capital letters will be sorted
#first before the other ones no matter the position,
#in the alphabetical order.

#sorting despite the caps.
test = ["cherry", "Kales", "apples", "Oranges", "Mangoes"]
print("\n")
print("Sorting without the caps")
test.sort()
print("initial : ",test)
test.sort(key = str.lower)
print("after : ",test)

#reversing the order of a list
print("\n")
print("Reversing the order of a list")
print("Initial : ",mylist)
mylist.reverse()
print("After : ",mylist)