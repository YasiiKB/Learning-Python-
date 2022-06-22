print ("Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature. \n")

#get the temperature in Celsius
TC = input("What's the temperature?")
TC = float(TC)
#convert to Fahrenheit and print
TF = (TC*9)/5+32
print("\nThat's",TF,"°F!")
