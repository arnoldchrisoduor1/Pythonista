arnoldDict = {"fName": "Arnold", "lName" : "Oduor", "address" : "123 Main St"}

print("My name : ",arnoldDict["fName"])

arnoldDict["address"] = "125 North St"

arnoldDict['city'] = 'Kisumu'

print("Is there a city : ", 'city' in arnoldDict)

print(arnoldDict.values())
print(arnoldDict.keys())

for k, v in arnoldDict.items():
    print(k, v)

print(arnoldDict.get("mName", "Not there!"))

arnoldDict.clear()

employees = []
fName, lName = input("Input the employee name : ").split()

employees = {"fname" : fName, "lname" : lName}

print(employees)