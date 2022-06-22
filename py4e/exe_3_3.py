print("Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the table:")
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F

#get the score and convert them
s= input("Enter your Score: ")
try:
    fs=float(s)
except:
    print("Error, please enter numeric input!")
    quit()
#checking the range

#try:
#    fs>=0.0
#    fs<=1.0
#except:
#    test=-1
#if test<0:
#    print("Error, Please enter a number within the range!")
## I think this try block isn't working cause the result is not assigend to anything. It's just fs>=0.
if fs<=0.0 or fs>=1.0:
    print("Error, Please enter a number within the range!")
else:
#Converting the score
    if fs>=0.9:
        print("A")
    elif fs>=0.8:
        print("B")
    elif fs>=0.7:
        print("C")
    elif fs>=0.6:
        print("D")
    elif fs<0.6 and fs>0.0:
        print("F")
