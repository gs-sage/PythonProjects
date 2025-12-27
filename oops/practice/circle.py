class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * (self.radius ** 2)
        return area
    
    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter
    

circle = Circle(4)
print(f"Area of circle : {circle.area()}")
print(f"Perimeter of circle : {circle.perimeter()}")
