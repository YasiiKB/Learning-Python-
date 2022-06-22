#Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error
#message and skip to the next number.
#while True:
#    number= input("Enter a Number: ")
#    try:
#        number=float(number)
#    except:
#        print("Invalid Number!")
#        quit ()
#    if line [0] == '#'
#        continue
#    if number == 'done' #this won't work here, cuz I have already turned number to a float!
#        break
#count=0 #better to intorduce them at the top of the code (as always!)
#sum=0
#average=0
#for number in [number]
#    count=count+1
#    sum= sum+number
#    average=sum/count
#print("Count:", count \n"Sum:", sum \n"average:", average)
#*************** GOOD CODE*************************#
count=0
sum=0
while True:
    number= input ('Enter a Number:')
    if number == 'done':
        break
    try:
        fnumber=float(number)
    except:
        print('Invalid Number')
        continue
    count=count+1
    sum=sum+fnumber
print(count,sum,sum/count)
