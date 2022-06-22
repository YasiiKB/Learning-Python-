#Rewrite the program that prompts the user for a list of
#numbers and prints out the maximum and minimum of the numbers at
#the end when the user enters “done”. Write the program to store the
#numbers the user enters in a list and use the max() and min() functions to
#compute the maximum and minimum numbers after the loop completes.
numlist=list()
while True:
    number =input('Enter a Number:')
    if number == 'done': break
    try:
        fnumber=float(number)
    except:
        print('Invalid input!')
        continue
    numlist.append(fnumber)
print('Maximum=',max(numlist))
print('Minimum=',min(numlist))
#print ('Average=',sum(numlist)/len(numlist))
