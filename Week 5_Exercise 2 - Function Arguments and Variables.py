#2.1. Sum of numbers (3 points)


def summ(num):
    return sum(num)

list_my = [1,2,3,4]


print("The sum of the numbers in the list is", summ(list_my))



#2.2. Number power (3 points)

def number_power(first_num,second_num):
    return first_num ** second_num
first = int(input("Input first number: "))
second = int(input("Input second number: "))
print("The power of these two numbers are",number_power(first,second))


#2.3. Tax function (3 points)

def price_with_tax(a):
    return a * 1.07
price = int(input("Input price of item: "))
print(f"The price of item is {round(price_with_tax(price),2)} with tax")


#2.4. Average function (3 points)

def average(num1, num2, num3):
    my_sum = num1 + num2 + num3
    avg = my_sum / 3
    return avg

no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))
no3 = int(input("Enter third number: "))
print("The average of these numbers entered are :", average(no1, no2, no3))