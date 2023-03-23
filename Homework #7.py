#Exercise #1: (5 points)


import datetime

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):

        self.name = name

        self.surname = surname

        self.birthdate = birthdate

        self.address = address

        self.telephone = telephone

        self.email = email


    def age(self):

        today = datetime.date.today()

        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):

            age -= 1

        return age


person = Person(

    "Jane",

    "Doe",

    datetime.date(1992, 3, 12), # year, month, day

    "No. 12 Short Street, Greenville",

    "555 456 0987",

    "jane.doe@example.com"

)


print(person.name)

print(person.email)

print(person.age())


# Explain what the following variables refer to, and their scope:


# Person - name of class which is used to define a blueprint for creating objects with the above attributes.
# person - instances of the Person class which is created by calling the constructor method - __init__
# surname - This is an attribute from Person class that represents the last name of an individual
# self - This is a reference to the current instance of the class that is accessed which is used for accessing objects attributes and methods within the class.
# age (the function name) - name of the method that quantifies age of a person
# age (the variable used inside the function) - a local variable used to store the age
# self.email - an attribute of the Person class that represents the email address, self is used as a reference of the current class
# person.email - an attribute of the Person class that represents the person's email address. It is accessed using person instance of the class previously created.



#Exercise #2: (5 points)


class Person:


    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        self.recalculate_age()

    def recalculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        self.age = age
        self._age_last_recalculated = today

    def age(self):
        if datetime.date.today() > self._age_last_recalculated:
            self.recalculate_age()
        return self.age


#Exercise #3: (5 points)


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

square2 = Square(10)
print(square2.area())

square2.side = 20
print(square2.area())



#Exercise #4: (5 points)


#Use the dir function on the instance.
print("dir() on the instance:")
print(dir(person))

#Then use the dir function on the class.
print("dir() on the class:")
print(dir(Person))

# What happens if you call the __str__ method on the instance? Verify that you get the same result
# if you call the str function with the instance as a parameter.
print("__str__method on the class")
print(person.__str__())

# What is the type of the instance?
print("type of the instance:")
print(type(person))

# What is the type of the class?
print("type of the class:")
print(type(Person))

# Write a function which prints out the names and values of all the custom attributes of
# any object that is passed in as a parameter. (see vars() hint.)
def print_custom_attributes(obj):
    for k, v in __dict__.items():
        print(k, ":", v)
# print("custom attributes of the person instance:")
# print_custom_attributes(person)


string = "Hello World"

#Exercise #5: (5 points)

class ReverseStrings:
    def __init__(self, strings):
        self.strings = strings

    def reversing_words(self):
        word = self.strings.split()
        word.reverse()
        return " ".join(word)

string = "Hello World"
reversing = ReverseStrings(string)
reversed = reversing.reversing_words()
print(reversed)


#Exercise #6: (5 points)
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

radiuss = Circle(5)
print(f"Area: {round(radiuss.area(),2)}")

print(f"Perimeter: {round(radiuss.perimeter(),2)}")


#Exercise #7: (5 points)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_rectangle(self):
        return self.length * self.width

areas = Rectangle(5,5)
print(f"Area of rectangle: {areas.area_rectangle()}")


#Exercise #8:

class Line:
    def __init__(self, coo1, coo2):
        self.coo1 = coo1
        self.coo2 = coo2

    def distance(self):
        x1, y1 = self.coo1
        x2, y2 = self.coo2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def slope(self):
        x1, y1 = self.coo1
        x2, y2 = self.coo2
        return (y2 - y1) / (x2 - x1)

coordinate_1 = (2,2)
coordinate_2 = (3,3)

li = Line(coordinate_1, coordinate_2)
print(f"Distance: {round(li.distance(),2)}")
print(f"Distance: {round(li.slope(),2)}")



#Exercise #9:


def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result

number_prompt = int(input("Enter a number: "))

while number_prompt != 1:
    number_prompt = collatz(number_prompt)
