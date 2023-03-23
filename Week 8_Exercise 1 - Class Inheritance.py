#1.1. Ice Cream Shop inherits from Restaurant (5 points)


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} restaurant serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def get_flavors(self):
        print("Our available ice cream flavors are: ")
        for flavor in self.flavors:
            print(f"- {flavor}")

#Restaurant instance
restaurant = Restaurant("YaoMing", "Asian")

#attributes and methods
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#icecream stand instance
ice_stand = IceCreamStand("COLD COLD ICE","Ice Cream",["Chocolate", "Strawberry", "Vanilla"])


#icecream get flavors
ice_stand.get_flavors()



#1.2. Admin inherits from User (5 points)


class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        print(f"User's name is {self.first_name} {self.last_name}. Gender is {self.gender} And is {self.age} years old")

    def greet_user(self):
        print(f"Hello {self.first_name}, how is your day?")

class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Admin {self.first_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# create User instances
user1 = User("Joe", "Smoe", 22, "male")
user2 = User("Bob", "Marley", 66, "male")
user3 = User("Rachel", "Ray", 50, "female")



# call User methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

# create Admin instance
admin = Admin("Captain", "Marvel", 999, "non-binary")

# Call admin methods
admin.describe_user()
admin.show_privileges()