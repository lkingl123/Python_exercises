#1.1. Hello World (again) (3 points)

def user_name():
    input_prompt = input("What is your username?")
    print(f"Hello, {input_prompt}")

user_name()


#1.2. Dog Years (3 points)


def dog_age():
    dog_ages = input("What is the dog's age?")
    multiplied = int(dog_ages) * 7
    print(f"Dog's age in human years is {dog_ages}, Dog's age in dog years is {multiplied}")

dog_age()


#1.3. Purchase (3 points)

def purchases():
    number_purchases = input("How many items do you wish to purchase?")
    print(f"User wishes to purchase {number_purchases} item or items")

purchases()