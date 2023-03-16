#Enter the investment amount, amount of years and the expected interest rate
invest = input("What's the investment amount: ")

invest  = int(invest)

time = input("For how long will the money be there: ")

time = int(time)
time = time + 1

rate = input("What rate do you expect: ")

rate = float(rate)

print("Calculating your investment of {} at {} interest rate compounding for {} year(s)".format(invest,rate,time))

#Each year we add the investment to the calculated rate
for y in range(time):
    interest = invest * (rate/100) * time
    compound = invest + interest

#Print out the money earnings after the input years

time  = time - 1

print("Your Investment after {} year(S) is {}".format(time,compound))
