''' With the help of https://www.geeksforgeeks.org/generating-strong-password-using-python/ '''

import random 
import array

def pass_generator(length):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    lowcase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
    upcase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
    
    #combine all the characters into one array 
    combined_list = digits + lowcase + upcase + symbols 
    
    #randomly select one character from each list
    random_digit = random.choice(digits)
    random_lowcase = random.choice(lowcase)
    random_upcase = random.choice(upcase)
    random_symbols = random.choice(symbols)

    #combine the four random characters 
    temp_pass = random_digit + random_lowcase + random_upcase + random_symbols

    # if the length is shorter than four characters (Shouldn't be, but just in case): 
    if length <= 4:
        # convert temporary password into array ('u' is data type, characters, and temp_pass is value list that will turn into an array)
        temp_pass_list = array.array('u', temp_pass)

        # shuffle the array to prevent it from having a consistent pattern where the beginning of the password is predictable
        random.shuffle(temp_pass_list)
    
        password = ""
        for i in temp_pass_list:
            password += i 

    # if the length is longer than four characters (length - 4 will not raise an error anymore)
    if length > 4:
        #repeat the selection to get the desired password length
        for i in range (length - 4):
            temp_pass = temp_pass + random.choice(combined_list)

            # convert temporary password into array 
            temp_pass_list = array.array('u', temp_pass)

            # shuffle the array to prevent it from having a consistent pattern where the beginning of the password is predictable
            random.shuffle(temp_pass_list)
        
        password = ""
        for i in temp_pass_list:
            password += i 
        
    return password

# get the user's inputs
print('*** Welcome to Password Generator! ***')
num_passwords = input('How many passwords do you need? ')
password_length = input('How long should they be (min 4 Charachters)? ')

while True:

    # check the inputs
    try: 
        num_passwords = int(num_passwords)
        password_length = int(password_length)
    except:
        print("Invalid Input. Try Again!")
        break 

    # make as many password as requested
    print('\nHere are your passwords: ') 

    for i in range (0 , num_passwords):
        print(pass_generator(password_length))
        i -=1 
        
    break