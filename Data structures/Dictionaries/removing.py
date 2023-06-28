#using the pop() method
thisdict = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 2020
}

print("Initial: ",thisdict)
thisdict.pop("Model")
print("After: ",thisdict)

#popitem() removes the last inserted item
print("\n")
print("Using the popitem method")
ndict = {
    "name" : "arnold",
    "age" : 19,
    "last": "oduor",
    "middle": "chris",
    "group" : "youth"
}

print("Initial: ",ndict)
ndict.popitem()
print("After: ",ndict)

#del removes the item thats stated
print("\n")
print("Using the del method")
print("Initial: ",ndict)
del ndict["last"]
print("After: ",ndict)
#del can also be used to completely delete 
#a dictionary.