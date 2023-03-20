def rec_area():
    width = float(input("Give the width : "))
    length = float(input("Give the length : "))

    area = width * length

    print("The area is = ",area)


def circ_area():
    radius = float(input("Please give the radius : "))
    pi = 3.14

    area = radius * radius * pi

    print("The area is {:.2f}",area)


def get_area(shape):
    shape = shape.lower()

    if shape == "rec":
        rec_area()
    if shape == "circ":
        circ_area()
    else:
        print("Sorry we could not find your shape")


def main():
    shape = input("For which shape do you want to find the area for")

    get_area(shape)


main()
