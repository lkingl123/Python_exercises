#3.1 Input with a for-loop (4.5 points)


quantity = int(input("How many numbers do you want to add? "))
total = 0
for i in range(quantity):
    number = int(input("Enter a number to add: "))
    total += number
    print(number)

print("The total is:", total)



#3.2 Find the vowels – for loop (4.5 points)

word_phrase = input("Enter a word or a phrase: ")
total = 0
vowels_found = []
for loop in word_phrase:
    if loop == "a" or loop == "e" or loop == "i" or loop == "o" or loop == "u":
        total += 1
        vowels_found.append(loop)
print("The total vowels in the word or phrase is: ", total)
print("Vowels found: ",vowels_found)

