#Exercise #1: (6 points)

try:
    with open("most_popular_words_in_english.txt", "r") as file:
        my_var = file.read()

    word_list = my_var.split("\n")

    user_word = input("Enter a word you are searching for in this text: ")

    if user_word in word_list:
        print(f"'{user_word}' is one of the most popular words in english")
    else:
        print(f"'{user_word}' is not one of the most popular words in english")

except:
    print("Something went wrong!")





#Exercise #2: (6 points)

username = input("Enter a username: ")
password = input("Enter a password: ")

with open("security.txt", "w") as file:
    file.write(username + "\n")
    file.write(password + "\n")

print("Username and password has been stored in security.txt")



#Exercise #3: (6 points)


with open("security.txt", "r") as file:
    username = file.readline().strip()
    password = file.readline().strip()

input_username = input("Enter username : ")
input_password = input("Enter password : ")

if input_username == username and input_password == password:
    print("Login successful!")
else:
    print("Incorrect username or password.")




#Exercise #4: (6 points)


with open("testscores.txt", "r") as file:
    lines = file.readlines()

for i in range(0, len(lines), 4):
    name = lines[i].strip()
    score1 = float(lines[i + 1].strip())
    score2 = float(lines[i + 2].strip())
    score3 = float(lines[i + 3].strip())
    total = (score1 + score2 + score3) / 3
    print(f"{name} has an average score of {total:.2f}")
