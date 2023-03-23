#Exercise #1:

def topOrBottom():
    print(" #####")

def middleLines():
    print(" #  #")

def lines1():
    print(" # #")

def lines2():
    print("  #")

def printPattern():
    topOrBottom()
    middleLines()
    lines1()
    lines2()
    lines1()
    middleLines()
    topOrBottom()

printPattern()



#Exercise #2:


def feet_inches(ft):
    inches = ft * 12
    return inches


def feet_meters(ft):
    meters = ft * 0.3048
    return meters

for i in range(10):
    ft = i
    inches = feet_inches(ft)
    meters = feet_meters(ft)
    meters_dec = round(meters, 4)
    print(f"{ft} ft:")
    print(f".. {inches} inches")
    print(f".. {meters_dec} meters")



#Exercise #3:

import random

def sided_dice_roll(num):
    die1 = random.randint(1, num)
    die2 = random.randint(1, num)
    return sorted([die1,die2])

dice_sides = [6,7,8,9,10]

for sides in dice_sides:
    rolls = sided_dice_roll(sides)
    print(f"{sides} sided dice roll: {rolls[0]} & {rolls[1]}")


#Exercise #4:

# This is a guess the number game.
import random

# use the random.randint() function to generate a random number between 1 and 20.

secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess. ')
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low. ")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

if guess == secretNumber:
    print(f"Good job! You guessed my number in {guessesTaken} guesses!")
else:
    print(f"You are out of guesses. And the number I was thinking of is {secretNumber}")