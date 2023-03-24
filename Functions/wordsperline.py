import os

with open("newdata.txt", mode = "w", encoding="utf-8") as myFile:
    myFile.write("This is data\nThis is another data\nAnd yet another line of data")

with open("newdata.txt", encoding="utf-8") as myFile:

    lineNum = 1
    while True:
        line = myFile.readline()

        if not line:
            break

        print("Line", lineNum, ":", line,end="")
        lineNum += 1
print()
print()
with open("newdata.txt", encoding="utf-8") as myFile:
    word = 1
    while True:
        line = myFile.readline()
        if not line:
            break
        word = line.split()
        for w in word:
            l = len(w)
            print("Word : ", w, ":", "Length : ", l)