import random

playing = True
number = str(random.randint(10, 20))

print("I will generate a number between 10 and 20 for you and you have to guess the number one digit at a time")
print("The game will ends when you get 1 hero!")

while playing:
    guess = input ("Give me your best guess: ")

    if number  == guess:
        print("You got it!")
        print("The number was: ", number)
        break
    else:
        print("Wrong Guess")
