#JSON is a syntax for storing and exchanging data written,
#in javascript style.

import json

#converting json to python
print()
print("Converting json to python.")
#random json file.
x = '{"name": "Arnold", "age" : 9, "Location" : "Awasi"}'
#convert to python dictionaries.
y = json.loads(x)
print(y["age"])

#Coverting from python to json.
print()
print("Converting from python to json.")
b = {
    "name" : "cally",
    "Location" : "Chemelil",
    "Age" : 7
}

c = json.dumps(b)
print(c)

#Converting python strings into json strings.
print()
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print()

#Converting a python dictionary containing all the, 
#legal data types.
print("Converting python cntaining all the legal data types into Json")
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True))