# Place your answer to Exercise_05 in this file
# Do not rename or remove this file
import math

length = float(input("Please enter the length of the wall:\n"))
height = float(input("Please enter the height of the wall:\n"))
print(f"You require {math.ceil((length*height)/20)} cans of paint.")