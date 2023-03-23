import math

#2.1. The simplest class: (5 points)


class Simplest:
    pass


# a. Using the code below, what type is this object?

print(type(Simplest))
# <class 'type'>

# b. Create an instance of Simplest to a variable called simp. What type is simp?

simp = Simplest()
print(type(simp))
# <class '__main__.Simplest'>


#2.2. Person Class: (5 points)


class Person:

    first_name = ""
    middle = ""
    last_name = ""

    def format_name(self):
        return (f"{first_name} {middle} {last_name}")


p = Person()
first_name = "King"
middle = "L"
last_name = "Loke"
print(p.format_name())


class Cylinder:

    def set_height_radius(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        return round(self.height * math.pi * (self.radius**2), 1)

    def surface_area(self):
        top = math.pi * (self.radius**2)
        return round((2 * top) + (2 * math.pi * self.radius * self.height), 1)


mycyl = Cylinder()
mycyl.set_height_radius(2,3)
print(mycyl.volume())

print(mycyl.surface_area())

