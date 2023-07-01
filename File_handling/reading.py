#using the read() command.
print()
print("Using the read() command")
f = open("demofile.txt", "rt")
print(f.read())
f.close()
#To open a file in a different location we put the ,
#directory name instead of the filename.

#Reading the firts 5 characters of the file.
print()
print("Reading the first 5 characters of the file")
f = open("demofile.txt", "rt")
print(f.read(5))
f.close()

#Reading a single line using the readline command.
print()
print("Reading a single line using the readline() command")
f = open("demofile.txt", "rt")
print(f.readline())
f.close()

#to read two we call the print statement twice.

#Reading the whole file line by line we use the for loop.
print()
print("Looping through all the lines using the for loop.")
f = open("demofile.txt", "rt")
for x in f:
    print(x)

f.close()
