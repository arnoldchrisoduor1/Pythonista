#try- block lets you test a code for errors.
#except - block lets you handle the errors.
#else - block lets you execute the code when there's no error.
#finally - block lets you execute the code irregadless of the try and except blocks.


print()
print("Simple try statement.")
try:
    print(x)
except NameError:
    print("The variable has NOT been defined")
except:
    print("An unknown error occurred")

#when no error occurs.
print()
print("When no error occurs.")
try:
    print("Hello")
except:
    print("Unknown error detected")
else:
    print("Simulation complete")

#Using finally regardless of  the outcome.
print()
print("Using the finally regardless of the except.")
try:
    print(y)
except:
    print("An error occurred")
finally:
    print("The 'try except' is finished")

#Writing to a file.
print()
print("Writing to a file")
try:
    f = open(demofile.txt)
    try:
        f.write("This is a demo text in a demo file.")
    except:
        print("Something went wrong while writing to the file.")
    finally:
        f.close()
except:
    print("Error opening the file")

#Raising an exception.
print()
print("Raising an exception")
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

#rasing a TypeError error
print()
print("Raising a TypeError Exception.")
k = "hello"
if not type(k) is int:
    raise TypeError("Only integers are allowed")