#python dictinaries
ndict = {
    "brand" : "Ford",
    "Year" : 1998,
    "Model": "Mustang"
}
#ordered, changeable and does not allow for duplicstes.

print(ndict)

#dictionary length
print("\n")
print("dictionary length")
print(len(ndict))

#values can be of any data type
print("\n")
print("Dict of any data type")
thisdict = {
    "model" : "Mustang",
    "Brand" : "Ford",
    "Year" : 1998,
    "colors" : ["red", "yellow", "white"]
}
print(thisdict)

#the dict constructor
print("\n")
print("The dict constructor")
mydict = dict(name = "John", age = 36, country = "Norway")
print(mydict)
