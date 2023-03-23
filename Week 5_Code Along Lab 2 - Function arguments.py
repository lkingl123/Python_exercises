# Week 5
# Code along 2
# functions and arguments

def format_name(first_name, last_name):
    return first_name + " " + last_name

first = input("What is your first name? ")
last = input("What is your last name?")
results = format_name(first, last)
print("Hello", results)



def average(num1, num2, num3):
    my_sum = num1 + num2 + num3
    avg = my_sum / 3
    return avg

avg = average(5,18,45)
print(avg)



def func(num1, num2):
    if num1 < 0:
        return "Please provide a non-negative number"
    else:
        return num1 + num2

print(func(-1,20))



def print_dict(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())

    for i in range(0, len(keys)):
        k = keys[i]
        v = values[i]
        print(k,v)

example_dict = {
    "name": "Thor",
    "age": "25"
}

print_dict(example_dict)


def sum_two_numbers(a,b):
    return a + b
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(sum_two_numbers(num1,num2))


def multiply_by(a,b=2):
    return a * b
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(multiply_by(num1,num2))
print(multiply_by(2,b=4))

def example(*args):
    print(type(args))
    print(args)

example(1,23,454,2,45,4)


def func(**kwargs):
    print(type(kwargs))
    print(kwargs)

func(a=1, b=2, c=3, d=4)




