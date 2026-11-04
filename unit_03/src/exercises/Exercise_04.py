# Place your answer to Exercise_04 in this file
# Do not rename or remove this file

copies = int(input("Please enter the number of copies of the software you wish to purchase:\n"))
discount = 0

if copies<=4:
    discount = 0
elif copies<=9:
    discount = 10
elif copies<=19:
    discount = 20
elif copies<=49:
    discount = 30
elif copies<=99:
    discount = 40
else:
    discount = 50

total = (copies*99)*((100-discount)/100)
print(f"You have been given a {discount}% discount on the normal price of £99.")
print(f"The total cost is £{total:.2f}.")