#deleting the file by importing the os.
import os

f = open("thisfile.txt", "x")
f.close()

if os.path.exists("thisfile.txt"):
    print("File exists.")
    print("Deleting file____")
    os.remove("thisfile.txt")
else:
    print("Error! Could not find file")

#deleting a whole folder using the rmdr command.
#os.rmdir("myfolder")