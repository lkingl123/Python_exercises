# Week 7
# Code along 2

import functions as func

class First_Class:

    # #print("Hello World OOP!")
    # var = "Hello"
    # if var = "Hello":
    #     print("this works?")

    def hello(self, x):
        print("Hello World OOP!", x)

    def hello_again(self, x):
        print(x)


f = First_Class()
f.hello("Mary")
f.hello_again("John")


class Student:


    first_name = ""
    last_name = ""
    is_graduated = False


student_a = Student()
student_a.first_name = "King"
student_a.last_name = "Loke"
# student_a.is_graduated = True
print(func.booleanYesNoConverter(student_a.is_graduated))
print(student_a.first_name,student_a.last_name)
