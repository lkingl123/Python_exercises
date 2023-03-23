# Week 2
# Code along 2
# part 1

print(True)
print(type(True))
print(False)
print(1 == 1) #true
print(1 == 2) #false
print(1 != 2) #true
print(1 != 1) #false
print(1 < 2) #true
print(1 > 2) #false
print(1 > 2 and 2 < 5) #false
print(not 1 > 2 and not 2 < 5) #false


# a = None
# print(a != None and a > 0)


# Part 2
x = -1
if x > 0:
    print("x is positive")
else:
    print("x is negative")


print("This line will always print")


x = -1

if x > 0:
    print("x is positive!")
elif x == 0:
    print("x is 0")
else:
    print("x is negative")


x = 7

if x > 0:
    print("x is positive")

    if x % 2 == 0:
        print("x is even!")
    else:
        print("x is odd!")

else:
    print("x is not positive")