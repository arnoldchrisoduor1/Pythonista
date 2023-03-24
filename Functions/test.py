import os

with open("mydata.txt", mode = "w", encoding="utf-8") as myFile:
    myFile.write("Some text\nAnother text\nAn even more random text\nThis is the last line of the random texts")

with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())

#print(myFile.closed)
#print(myFile.name)
#print(myFile.mode)

os.rename("mydata.txt", "mydata2.txt")
os.remove("mydata2.txt")
os.mkdir("mydir")
os.chdir("mydir")

print("Current working directory : ",os.getcwd())

os.chdir("..")
print("current directory : ",os.getcwd())
os.rmdir("mydir")