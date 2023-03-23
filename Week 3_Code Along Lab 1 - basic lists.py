# Week 3
# Code along 1


# create an empty list
empty_list = []

my_list = [95,3.2,"Marvel",17,-4]

print(my_list[2])
print("list contents",my_list)

second_list = [100, 101]
print("second list",second_list)

second_list = second_list * 2
print("second list repeated x2",second_list)

# merge the lists
big_list = my_list + second_list
print("big list", big_list)


characters = ["Spider-man", "Thor", "Ironman", "Loki", "Hulk", "Black Panther", "Captain America"]
print(characters)
print(len(characters))
print(characters[2])
print(characters[1:3]) #Thor and Ironman
print(characters[1:5])
print(characters[-3]) #hulk
print(characters * 2)
print(characters[::3]) #Spiderman, Loki, Captain America
print(characters[2][-1]) #n