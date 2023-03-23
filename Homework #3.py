#Exercise 1: (3 points)

grades = [90,100,70,45,76,84,93,21,36,99,100]

count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_f = 0

for grade in grades:
    if grade >= 90 and grade <= 100:
        count_a += 1
    elif grade >= 80 and grade < 90:
        count_b += 1
    elif grade >= 70 and grade < 80:
        count_c += 1
    elif grade >= 60 and grade < 70:
        count_d += 1
    else:
        count_f += 1

print("A:", count_a)
print("B:", count_b)
print("C:", count_c)
print("D:", count_d)
print("F:", count_f)


#Exercise 2: (3 points)

grades = [93, 74, 66, 98, 34, 75, 79, 83, 84, 91, 12, 69, 72]
new_grades = []

for grade in grades:
    if grade >= 90 and grade < 100:
        new_grades.append(grade)
    elif grade >= 80 and grade < 90:
        new_grades.append(grade + 2)
    elif grade >= 70 and grade < 80:
        new_grades.append(grade + 5)
    else:
        new_grades.append(grade + 8)
print(new_grades)


#Exercise 3: (3 points)

Sales_for_the_week = []

Sunday = int(input("Enter sales for Day #1: "))
Monday = int(input("Enter sales for Day #2: "))
Tuesday = int(input("Enter sales for Day #3: "))
Wednesday = int(input("Enter sales for Day #4: "))
Thursday = int(input("Enter sales for Day #5: "))
Friday = int(input("Enter sales for Day #6: "))
Saturday = int(input("Enter sales for Day #7: "))

Sales_for_the_week.append(Sunday)
Sales_for_the_week.append(Monday)
Sales_for_the_week.append(Tuesday)
Sales_for_the_week.append(Wednesday)
Sales_for_the_week.append(Thursday)
Sales_for_the_week.append(Friday)
Sales_for_the_week.append(Saturday)

print("Sales for the week: ",Sales_for_the_week)


#Exercise 4: (3 points)

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#Extract the first 3 elements of the list into a new list
first_3 = my_list[:3]
print("first three elements: ",first_3)

#Extract the characters b, c, and d into a new list
bcd = my_list[1:4]
print("b,c,d: ",bcd)

# Extract the last 4 characters into a new list
last_four = my_list[-4:]
print("Last four elements: ",last_four)


#Exercise 5

products = ["apple", "pear", "peach", "banana"]

product_name = input("Enter the name of a product: ").lower()

if product_name in [p.lower() for p in products]:
    print(f"{product_name} is in our inventory.")
else:
    print(f"{product_name} is not found.")


#Exercise 6


similar = []

a = [1,2,3,4,5]
b = [2,3,10,11,12,1]



for i in a:
    if i in b:
        similar.append(i)

print(similar)


#Exercise 7


names = []

while True:
    name = input("Enter a name: (end to stop)")
    if name.lower() == "end":
        break
    if name in names:
        print(f"{name} has already been entered")
    else:
        names.append(name)

print("Names: ",names)


#Exercise 8

products = ["apple", "pear", "peach", "banana"]

while len(products) > 0:
    product_name = input("Enter the name of a product (or 'end' to stop): ").lower()
    if product_name == "end":
        break
    if product_name in [p.lower() for p in  products]:
        products.remove(product_name)
        print(f"{product_name} has been removed from the inventory.")
        print("Current products: ", products)
    else:
        print(f"{product_name} is not currently in the inventory.")

print("Inventory is empty")


#Exercise 9


products = ['peanut butter', 'jelly', 'bread']

prices = [3.99, 2.99, 1.99]


product = input("Enter a product ('peanut butter', 'jelly', 'bread'): ")

if product in products:
    index = products.index(product)
    price = prices[index]

    print(f"{product} cost ${price}")

else:
    print("Price not available for this product")


#Exercise 10


num_students = int(input("How many students in the class? "))
num_assignments = int(input("How many assignments in the class? "))

for student_num in range(1, num_students + 1):
    student_total = 0
    for assignment_num in range(1, num_assignments + 1):
        score = int(input(f"Student #{student_num}\nAssignment #{assignment_num}: "))
        student_total += score
    student_avg = student_total / num_assignments
    print(f"Student #{student_num} earned an average of {student_avg}")
