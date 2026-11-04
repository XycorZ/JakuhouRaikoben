# Place your answer to Exercise_03 in this file
# Do not rename or remove this file

child = int(input("How many child tickets would you like?\n"))
adult = int(input("How many adult tickets would you like?\n"))
senior = int(input("How many senior tickets would you like?\n"))
print(f"Total Price: £{round((5*child+10*adult+8*senior),2)}")