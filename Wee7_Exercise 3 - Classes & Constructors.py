


#3.1. NumberSet Class (5 points)


class NumberSet:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

t = NumberSet(6, 10)






class Animal:
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def get_arms(self):
        return self.arms

    def get_legs(self):
        return self.legs

    def get_arms_legs(self):
        return self.arms + self.legs


human = Animal(2,2)
spider = Animal(4,4)
print(human.get_arms_legs())
print(spider.get_arms_legs())





class Cereal:

    def __init__(self, name, brand, fiber):
        self.name = name
        self.brand = brand
        self.fiber = fiber

    def instances(self):
        return f"Name is {self.name}, is produced by {self.brand}, {self.fiber} grams of fiber in every bowl!"


c1 = Cereal("Corn Flakes","Kellogg's",2)
c1_1 = c1.instances()
c2 = Cereal("Honey Nut Cheerios","General Mills",3)
c2_2 = c2.instances()
print(c1_1)
print(c2_2)
