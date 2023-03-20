norm = input("Please enter a text : ")

secret = ""

for char in norm:

    secret += str(ord(char)-23)
    

print("The secret message is :",secret)

norm = ""

for i in range(0,len(secret)-1,2):

    char_code = secret[i] + secret[i+1]

    norm += chr(int(char_code)+23)

print("The normal text is :",norm)
