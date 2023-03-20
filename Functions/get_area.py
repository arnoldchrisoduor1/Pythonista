def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    if shape == "circle":
        circle_area()
    else:
        print("Sorry shape area cannot be calculated!")


def rectangle_area():
    width = float(input("Give the width of the rectangle : "))
    length = float(input("Give the length of the rectangle : "))

    print("Rectangle area = ", str(width * length))


def circle_area():
    radius = float(input("Give the circle radius : "))
    pi = 3.14

    print("Circle are = ", str(pi * radius * radius))


def main():
    shape = input("Which shape do you want to find the area for : ")

    get_area(shape)


main()
