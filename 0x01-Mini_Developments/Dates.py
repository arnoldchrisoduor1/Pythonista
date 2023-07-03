#Display the current date
import datetime

print()
print("Showing the current date and time: ")
x = datetime.datetime.now()
print(x)

#Returning the name and year of the calendar.
print()
print("Returning the year and day of the calendar.")
a = datetime.datetime.now()
print(a.year)
print(a.strftime("%A"))
print()

#Creating datetime objects using the datetime() class,
#constructor.
print("Creating datetime objects.")
m = datetime.datetime(2020, 1, 13)
print(m)
print()

#using the strftime() to create readble dates.
print("Using 'strftime()' to create readable dates.")
n = datetime.datetime(2023, 1, 13)
print(n.strftime("%B"))