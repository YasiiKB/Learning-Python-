print("Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters ( hours and  rate).")

def computepay (h,r):
    if h>40:
        print("Overtime")
        ot= h-40
        otp=r*1.5
        pay = 40*r + ot*otp
    else:
        print("Regular Hours")
        pay =h*r
    return pay
#get the hours and the rate and convert them
hr= input("Enter Hours: ")
rt = input("Enter Rate: ")
try:
    thr=float(hr)
    trt=float(rt)
except:
    print("Error, please enter numeric input!")
    quit() #don't know how this changes things.
#Using the pay function
pay = computepay (thr,trt)
print("Pay:",pay)
