#1 Countdown (3 points)

i = int(input("Guess a number!"))
while i > 0:
  print(i)
  i -= 1

print("Done!")







#2 Shopping Total (3 points)

total_variable = 0
tax_variable = 0.08875
price = input("Enter the price of the item (or 'done' when finished): ")

while price != "done":
    if float(price) > 0:
        total_variable += float(price)
        tax_amount = float(price) * tax_variable
        total_variable += tax_amount
    else:
        print("Invalid price. Please enter a valid number.")
    price = input("Enter the price of the item (or 'done' when finished): ")

print("Total cost including tax is: $" + str(total_variable))

