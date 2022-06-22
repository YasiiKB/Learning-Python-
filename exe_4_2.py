print("Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.")
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
def computegrade (s):
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
#get the score and convert them
s= input("Enter your Score: ")
try:
    fs=float(s)
except:
    print("Error, please enter numeric input!")
    quit()
#checking the range
if fs<=0.0 or fs>=1.0:
    print("Error, Please enter a number within the range!")
else:
    computegrade (fs)
