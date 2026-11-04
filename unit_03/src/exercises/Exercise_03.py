# Place your answer to Exercise_03 in this file
# Do not rename or remove this file

convert = int(input("Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius:\n"))

if (convert != 1) and (convert!=2):
    print("ERROR: Invalid option")
else:
    if convert==1:
        temp = float(input("Please enter the temperature in Celsius:\n"))
        if temp>=0:
            print(f"{temp} Celsius is equivalent to {(9/5)*temp+32} Fahrenheit.")
        else:
            print("ERROR: You must enter a value of 0 or greater.")
        
    else:
        temp = float(input("Please enter the temperature in Fahrenheit:\n"))
        if temp>=0:
            print(f"{temp} Fahrenheit is equivalent to {(5/9)*(temp-32)} Celsius")
        else:
            print("ERROR: You must enter a value of 0 or greater.")

