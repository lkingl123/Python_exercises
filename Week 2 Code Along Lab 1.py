
# Week 2
# Code along 1
# this is a single line comment

"""
comments inside triple quote block
More comment on next line
and so forth
"""


a = "100"
b = "50.75"
c = "-3.2"

#convert the strings to numeric data types

d = int(a)
e = float(b)
f = float(c)


answer = d + e + f
print(answer)

# answer = a + b + c
# print(answer)

print("the sum of ", a, b, "and", c, "is", answer)


user_age = input("What is your age?")
user_name = input("What is your name")
print("Welcome to my program", user_name)
print("You are", user_age, "years old")