#Take in text input to encrypt

#Take in number to decide by how much the shift should be by

# A - Z 65 - 90

#if key is bigger or smaller than the unicode we add or subtract it by 26

#ord(letter)

#chr(code)

text = input("Please input the text to encrypt : ")

text = text.upper()
key = input("Please give the number or encryption shift : ")

key = int(key)
while key > 26:
    key = key - 26
    
print(key)

while  key <= 26 and key >= 0:

    encrypt = ""

    for char in text:
        encrypt += str(ord(char) + key)

    print("The message has been successfully encrypted : ",encrypt)

    print("Decrypting the Message")

    text = ""

    for i in range(0,len(encrypt)-1,2):
        new_code = encrypt[i] + encrypt[i+1]

        text += chr(int(new_code) - key)

    print("The Message was : ",text)
    break;
