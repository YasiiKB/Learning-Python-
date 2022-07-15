import re

# functions 
def add(num1, num2):
    output = num1 + num2
    return output

def sub(num1, num2):
    output = num1 - num2
    return output

def mult(num1, num2):
    output = num1 * num2
    return output

def dev(num1, num2):
    try: 
        output = num1 / num2
        return output
    except ZeroDivisionError:
        print("Sorry ! You are dividing by Zero ")
    
def pow(num1, num2):
    output = num1 ** num2
    return output

def percent(num1, num2):
    try: 
        output = (num1 / num2) * 100
        return output
    except ZeroDivisionError:
        print("Sorry ! You are dividing by Zero ")
    

# getting user's input
equation = input('Input: ').replace(" ","")

# separating the numbers and the operator
numbers = re.findall('[0-9]+', equation)
op= re.findall('\D', equation)
#print (len(op))

# we need this if loop to detect ** (not *)
if len(op) == 2:
    op = '**'
else: 
    op= re.findall('\D', equation)[0]

while True: 

    # checking user's input
    try:
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        
    except:
        print('Invalid input!')
        break

    # calculations
    if op == '+':
        print('Result:',add(num1, num2))

    elif op == '-':
        print('Result:',sub(num1, num2))

    elif op =='*':
        print('Result:',mult(num1, num2))

    elif op =='/':
        print('Result:',dev(num1, num2))

    elif op =='**':
        print('Result:',pow(num1, num2))

    elif op =='%':
        print(num1,'is',percent(num1, num2),'%','of', num2,'.')

    break






