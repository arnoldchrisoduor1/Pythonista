#nested dictionaries.
myfamily = {
    "child1":{
        "name":"linus",
        "age" : 4
    },
    "child2":{
        "name":"nadia",
        "age":7
    },
    "child3":{
        "name":"dennis",
        "age":9
    }
}

print(myfamily)

#creating a dictionary that will hold others.
print("\n")
print("A dictionari within a dictionary")
child1 = {
        "name":"linus",
        "age" : 4
    },
child2 = {
        "name":"nadia",
        "age":7
    },
child3 = {
        "name":"dennis",
        "age":9
    }
newfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(newfamily)

#accessing items in a nested family.
print("\n")
print("Accessing items in a nested family")
print(myfamily["child2"]["name"])