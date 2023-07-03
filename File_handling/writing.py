#appending to a file.
print()
print("Appending to a file")
f = open("demofile.txt", "a")
f.write("This is an appended line")
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()

#creating a new file
print()
print("Creating a new file")
f = open("myfile.txt", "x")
f.close()

print()
print("Writing to the newly created file")
try:
    f = open("myfile.txt", "w")
    f.write("This is a line")
    f.close()
    f = open("myfile.txt", "a")
    f.write("Appended line.")
    f.close()
except:
    print("Error could not create the file")
else:
    f.close()

f = open("myfile.txt", "rt")
print(f.read())