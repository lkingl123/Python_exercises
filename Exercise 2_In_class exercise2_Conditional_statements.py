#1. Password verification (2 points)

password_variable = "GoUtes!"

password_prompt = input("Please input your password")

if password_prompt == password_variable:
    print("Access Granted")
else:
    print("Access Denied")


#2. Voting Age (2 points)

voting_age = 18

age_prompt = input("What is your age?")
age_diff = int(voting_age) - int(age_prompt)

if int(age_prompt) >= voting_age:
    print("User can vote")
else:
    print("User can only vote in", str(age_diff), "years")


#3. Dress for Weather (2 points)

temperature_prompt = int(input("What is the temperature in Fahrenheit?"))

if temperature_prompt < 40:
    print("Wear a warm coat.")
elif temperature_prompt < 70:
    print("Wear a light jacket.")
elif temperature_prompt < 100:
    print("Wear something cool.")
elif temperature_prompt >= 100:
    air_conditioning = input("Do you have air conditioning at home? (yes/no)").lower()
    if air_conditioning == "yes" or air_conditioning == "y":
        print("Stay at home")
    else:
        print("Bummer, try a swimming pool.")


