print("Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.")
#Enter Hours: 45
#Enter Rate: 10
#   hint:475 = 40 * 10 + 5 * 15
#Pay: 475.0

#get the hours and the rate and convert them
hr= input("Enter Hours: ")
rt = input("Enter Rate: ")
hr=float(hr)
rt=float(rt)
#calculating the pay
if hr>40:
    print("Overtime")
    ot= hr-40
    otp=rt*1.5
    pay = 40*rt + ot*otp
else:
    print("Regular Hours")
    pay =hr*rt
print("Pay:",pay)
