import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again! Too low!")
        elif guess > random_number:
            print("Sorry, guess again! Too high!")
    print(f"You got it! You guessed {random_number} correctly!")

x = int(input("Give me a number: "))
print (f"Now the computer will pick a secret number between 1 and {x}!")
guess(x)
