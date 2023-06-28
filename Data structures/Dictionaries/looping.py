#looping through a dictionary.
car = {
    "brand": "ford",
    "model":"mustang",
    "year":2020
}

#looping keys.
print("Looping through the values")
for x in car.values():
    print(x)

print("\n")
print("looping through the keys")
for x in car.keys():
    print(x)

#looping thrpugh both the keys and values
print("\n")
print("Looping through the valuea and keys")
for x, y in car.items():
    print(x, y)

