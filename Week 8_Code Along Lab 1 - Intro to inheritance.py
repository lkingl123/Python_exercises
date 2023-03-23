# Week 8
# Code Along 1

class Person:
    _uNID = " "
    _address = " "
    _DOB = " "
    _email = " "
    _first_name = " "
    _last_name = " "


    def __init__(self, first_name, last_name, uNID):
        self._uNID = uNID
        self._first_name = first_name
        self._last_name = last_name

    def get_name(self):
        return f"{self._first_name} {self._last_name}"

class Student(Person):
    _courses = []


    def add_class(self, class_name):
        self._courses.append(class_name)

    def get_schedule(self):
        return self._courses


class Athlete(Student):
    _sport = " "

    def __init__(self, first_name, last_name, uNID, sport):
        super().__init__(first_name, last_name, uNID)
        self._sport = sport

class Staff(Person):
    _department = ""
    _salary = ""


    def __init__(self, first_name, last_name, uNID, salary):
        super().__init__(first_name, last_name, uNID)
        self._salary = salary


class Teacher(Staff):
    _courses_taught = []

    def assign_teaching(self, course):
        self._courses_taught.append(course)


    def schedule(self):
        return  self._courses_taught


student = Student("Supraja", "Dasari", "u1448122")
student.add_class("Python")
student.add_class("Economics")
print(student.get_schedule())


teacher = Teacher("John", "DeGrey", "u0983841", 100000)

teacher.assign_teaching("Python")
teacher.assign_teaching("Power Apps")
print(teacher.schedule())
