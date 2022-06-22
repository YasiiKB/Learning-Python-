import random

def computer_guess(x):
    low = 1
    high = x
    feedback = " "

    while feedback != "c":
        # high and low shouldn't be the same! If they are, it means the compuer has guessed the number already.
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #or low b/c low = high

        feedback = input (f"Is {guess} too high(H), too low (L) or just right (C)?").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"The compuer got it! It guessed {guess} correctly!")

x = int(input("Give me a number: "))
print (f"Now pick a secret number between 1 and {x}!")
computer_guess(x)
