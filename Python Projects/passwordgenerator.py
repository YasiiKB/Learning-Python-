import random 
import time

def password_generator(password_length):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,<>?/+=0123456789'
    password =''
    for c in range (password_length):
        password += random.choice(chars)
    print(password)

# get the user's inputs
print('Welcome to Password Generator!')
num_passwords = input('\nHow many passwords do you need?')
password_length = input('How long should they be?')

# check the inputs & run the password_generator function 
try: 
    num_passwords = int(num_passwords)
    password_length = int(password_length)

    # to make it more "natural" :)
    time.sleep(1)

    # generate passwords
    print('Your Passwords(s) are ready:')
    for passwords in range (num_passwords): 
        password_generator(password_length)

except:
    print("Invalid Input. Try Again!")