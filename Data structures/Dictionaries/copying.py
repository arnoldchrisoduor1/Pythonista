#using the copy method
car = {
    "brand":"ford",
    "model":"mustang",
    "year":2020
}

thisdict = car.copy()
print(thisdict)

#using the dict() method
print("\n")
print("Using the dict method")
mydict = dict(car)
print(mydict)