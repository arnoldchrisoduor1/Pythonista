
normal_text = input("Please give us a normal text : ")

secret_message = ""
new_text =""
for char in normal_text:

    secret_message += str(ord(char)-23)

for char in normal_text:
    new_text += str(ord(char))



print("The secret message is : ",secret_message)

normal_text = ""

for i in range(0,len(secret_message)-1,2):

    char_code =  secret_message[i] + secret_message[i+1]

    normal_text = chr(int(char_code)+23)

print("The original text :",normal_text)

    
