# Week 7
# Code along lab 7


class Student:

    # first_name = ""
    # last_name = ""
    is_graduated = False


    def __init__(self, fname, lname):

        try:
            self.first_name = fname
            self.last_name = lname

            if self.first_name!= None:
                self.first_name = fname

        except Exception as ex:
            print(ex)

    def say_hi(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    def format_name(self):
        return f"{self.first_name} {self.last_name}"

student_a = Student("King", "Loke")
student_a.say_hi()
print(student_a.format_name())
