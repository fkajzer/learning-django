class Circle():
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius**2 * Circle.pi

    def set_radius(self, radius):
        self.radius = radius

myc = Circle(3)

#myc.radius = 50
myc.set_radius(50)
print(myc.area())
