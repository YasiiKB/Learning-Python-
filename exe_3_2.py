print("Rewrite your pay program using try and except so that your program handles non-numeric input gracefully.")
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input

#Enter Hours: forty
#Error, please enter numeric input

#get the hours and the rate and convert them
hr= input("Enter Hours: ")
try:
    thr=float(hr)
except:
    thr=-1
if thr<0:
    print("Error, please enter numeric input!")
#the rest needs to be in this "else" block, otherwise when hours is not put in digits, the scond error will print out twice.
else:
    rt = input("Enter Rate: ")
    try:
        trt=float(rt)
    except:
        trt=-1
    if trt<0:
        print("Error, please enter numeric input!")
    else:
        #hr=float(hr)
        #rt=float(rt)
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
