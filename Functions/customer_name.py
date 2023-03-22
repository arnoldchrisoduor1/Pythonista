customer = []
answer = input("Enter Customer Name (y/n) : ")

while answer == 'y':
    fName, lName = input("Give the first and the last name : ").split()
    customer.append({"fName" : fName, "lName" : lName})
    answer = input("Enter Customer Name (y/n) : ")

for cust in customer:
    print(cust['fName'], cust['lName'])