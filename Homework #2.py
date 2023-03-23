


#Exercise 2.2:
#Exercise 2.1

value = input("Enter a coin value: Example(1,5,10,25,50) ")

if value == "1":
    print("That's a Penny!")
elif value == "5":
    print("That's a Nickle!")
elif value == "10":
    print("That's a Dime!")
elif value == "25":
    print("That's a Quarter!")
elif value == "50":
    print("That's a Half dollar!")
else:
    print("That’s not a valid coin!")


while True:
    number = input("Pick a number between 1 and 10 inclusive: ")
    try:
        number = int(number)
    except:
        print("Invalid input. Please pick a number between 1 and 10.")
    if number < 1 or number > 10:
        print("Invalid input. Please pick a number between 1 and 10.")
    else:
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")
        if number in [2,3,5,7]:
            print("Prime")
        else:
            print("Not prime")
        break

#Exercise 2.3:

while True:
    price = input("Input price of the item: ")
    try:
        price = float(price)
    except:
        print("Invalid input. Please use numbers. ")
    if price <= 0:
        print("Invalid input. Please use positive numbers. ")
    else:
        if price <= 10:
            print("No discount")
        elif price > 10 and price <= 50:
            print("Discount of 10%")
        else:
            print("Discount of 20%")
        break

#Exercise 2.4

start_num = int(input("Enter starting number: "))
end_num = int(input("Enter ending number: "))
even_odd = input("even or odd?: ")

if even_odd == "even":
    for i in range(start_num, end_num+1):
        if i % 2 == 0:
            print(i)

else:
    for i in range(start_num, end_num+1):
        if i % 2 != 0:
            print(i)

#Exercise 2.5

num_products = int(input("Enter number of products: "))

total = 0

for i in range(1, num_products+1):
    price = float(input(f"Enter price of product # {i}: "))
    total += price

print(f"Total cost: {total}")


#Exercise 2.6

total = 0
while True:
    price = float(input("Enter an item price: "))
    tax = round((price * 0.07),2)
    total_price = price + tax
    print(f"Tax on this item is {tax} ; total price is {total_price}")
    total += total_price
    another = input("Enter another price? (yes or no): ")
    if another != "yes":
        break

#Exercise 2.7

total = 0
while True:
    price = float(input("Enter an item price: "))
    tax = round((price * 0.07),2)
    total_price = price + tax
    print(f"Tax on this item is {tax} ; total price is {total_price}")
    total += total_price
    another = input("Enter another price? (yes or no): ")
    if another != "yes":
        break
print(f"Total amount due: ${round(total,2)}")
print(f"Total tax due: ${round((total * 0.07),2)}")


#Exercise 2.8

while True:
    answer = input("What is 2 + 2? ")
    if answer == "4":
        print("Correct!")
        break
    else:
        print("Wrong, try again.")

#Exercise 2.9

import random

while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question = "What is " + str(num1) + " + " + str(num2) + " equal? "
    answer = input(question)
    if int(answer) == num1 + num2:
        print("Correct!")
        break
    else:
        print("Wrong, try again.")






