import os

with open("mydata.txt", mode = "w",encoding="utf-8") as myFile:
    myFile.write("This is line of text\nAnother line of text\nAnother random line of text")

with open("mydata.txt", encoding="utf-8") as myFile:
    lineNum = 1

    while True:
        line = myFile.readline()

        if not line:
            break

        print("line", lineNum, ":",line, end="")

        lineNum += 1