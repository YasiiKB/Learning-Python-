#Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and and at the end prints out both the maximum and minimum of
#the numbers instead of the average. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
#message and skip to the next number.
count=0
sum=0
min = None
max = None
while True:
    number= input ('Enter a Number:')
    if number == 'done':
        break
    try:
        fnumber=float(number)
    except:
        print('Invalid Number')
        continue
    if min is None:
        min = fnumber
    elif fnumber < min:
        min = fnumber
    if max is None:
        max = fnumber
    elif fnumber > max:
        max = fnumber
    count=count+1
    sum=sum+fnumber
print(count,sum,min,max)
