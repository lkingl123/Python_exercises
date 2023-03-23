#1.1 Create Dictionaries (2.5 points)

birthday_data = {"Jake":"10/27/1995",
                 "King":"10/28/1995",
                 "Jason":"10/29/1995",
                 "Kong":"10/30/1995"}

for name in birthday_data:
    print(f"{name} is born in {birthday_data[name]}")


#1.2 Update Dictionaries (2.5 points)

birthday_data["Kong"] = "06/06/1980"
print(f"{name} is born in {birthday_data[name]}")


#1.3 Dictionary With Lists (2.5 points)]

seasons = {"Spring": ["March, April, May"],
           "Summer": ["June, July, August"],
           "Fall": ["September, October, November"]}

print(f"The value to the key 'Fall' is {seasons['Fall']}")


#1.4 Dictionary Merge

dictionary = {"Winter": ["December, January, February"]}
seasons.update(dictionary)
print(seasons)



