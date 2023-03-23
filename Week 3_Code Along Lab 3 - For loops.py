#Week 3
#Code Along Lab 3

fruit = "apples"
for x in fruit:
    print(x)
print("Done")
print(fruit[1])

total = 0
for i in range(10000):
    total += i
print("Sum of all numbers from [0, 10000]:", total)



dc_characters = ["Batman","Flash","Aquaman","Cyborg","Wonder Woman","Shazam"]

for item in dc_characters:
    print(item)


for item in range(len(dc_characters)):
    print(item)

for item in range(len(dc_characters)):
    dc_characters.append("Horus")

print(dc_characters)



