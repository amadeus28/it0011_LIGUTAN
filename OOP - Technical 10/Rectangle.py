class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth

def main():
    length = float(input("Rectangle length: "))
    breadth = float(input("Rectangle breadth: "))

    rectangle = Rectangle(length, breadth)
    print("Area of the rectangle:", rectangle.area())

main()