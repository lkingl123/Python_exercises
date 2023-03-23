#1. Change Calculator (2.5 points)

pennies_prompt = input("What is the penny amount?")
nickles_prompt = input("What is the nickle amount?")
dimes_prompt = input("What is the dime amount?")
quarters_prompt = input("What is the quarters amount")

total = float(pennies_prompt) * 0.01 + float(nickles_prompt) * 0.05 + float(dimes_prompt) * 0.1 + float(quarters_prompt) * 0.25

print("You have $",round(total,2))


#2. Currency Exchange (2.5 points)

exchange_rate = input("What is the exchange rate compared to USD? (example = 0.5)")
exchange_amount = input("What is the amount of money you want to convert?")

currency_calculation = float(exchange_amount) * float(exchange_rate)
print("The amount we currently have in the new rate is", round(currency_calculation,2))








