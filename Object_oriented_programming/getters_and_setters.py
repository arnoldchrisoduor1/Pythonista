class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the height")

        return self.__height

    @height.setter
    def height(self, value):

        if value.isdigit():
            self.__height = value
        else:
            print("please only enter a number for height")

    @property
    def width(self):
        print("Retrieving the width")

        return self.__width

    @width.setter
    def width(self, value):

        if value.isdigit():
            self.__width = value
        else:
            print("please only enter a number for width")

    def get_area(self):
        return int(self.__height) * int(self.__width)


def main():
    asquare = Square()

    height = input("Give the height : ")
    width = input("Give the width : ")

    asquare.height = height
    asquare.width = width

    print("Height : ", asquare.height)
    print("Width : ", asquare.width)

    print("The area is : ", asquare.get_area())


main()
