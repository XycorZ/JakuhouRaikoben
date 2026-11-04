# Place your answer to Exercise_02 in this file
# Do not rename or remove this file

temp = float(input("Please enter the temperature in Celsius:\n"))
if temp >= 0:
    print(f"{temp} Celsius is equivalent to {(9/5)*temp+32} Fahrenheit.")
else:
    print("ERROR: You must enter a value of 0 or greater.")