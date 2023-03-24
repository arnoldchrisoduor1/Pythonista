import os

with open("mydata2.txt", mode = "w", encoding="utf-8") as myFile:
    myFile.write("This is a data text\nThis is another data text\nThis is another line of text")

with open("mydata2.txt", encoding="utf-8") as myFile:
    word = 1
    while True:
        line = myFile.readline()
        if not line:
            break
        word = line.split()
        for w in word:
            l = len(w)
            print("Word : ", word, "length : ", l)
print()
print()

with open("mydata2.txt", encoding="utf-8") as myFile:
    lineNum = 1
    while True:
        line = myFile.readline()

        if not line:
            break
        print("Line", lineNum, ":", line, end="")
        lineNum += 1