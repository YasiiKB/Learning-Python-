print("Rewrite your pay program using try and except so that your program handles non-numeric input gracefully.")
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input

#Enter Hours: forty
#Error, please enter numeric input

#get the hours and the rate and convert them
hr= input("Enter Hours: ")
rt = input("Enter Rate: ")
try:
    thr=float(hr)
    trt=float(rt)
except:
    print("Error, please enter numeric input!")
    quit() #don't know how this changes things.
#calculating the pay
if thr>40:
    print("Overtime")
    ot= thr-40
    otp=trt*1.5
    pay = 40*trt + ot*otp
else:
    print("Regular Hours")
    pay =thr*trt
print("Pay:",pay)
