#take input of time,investment and rate

#calculate the interset per year and add to overall investment

invest = input("Please give the amount you wish to invest")
invest  = int(invest)

rate = input("Please give the rate you expect form this investment")
rate  = float(rate)

time = ("For how long will you be saving your money with us ? :")
time = int(time)

#calculating interest

time = time + 1

for n in range(time):
    interest = invest * (rate/100)
    compound = invest + interest

time = time - 1

print("Your investment after {} year(s) is {} ".format(time,compound))
