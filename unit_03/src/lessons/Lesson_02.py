# Place your answer to Lesson_02 in this file
# Do not rename or remove this file

num = int(input("Please enter a number:\n"))
if (num%3==0) and (num%5==0):
    print("Your number is divisible by 3 and 5.")
else:
    if (num%3==0) and (num%5!=0):
        print("Your number is divisible by 3 and NOT by 5.")
    elif (num%3!=0) and (num%5==0):
        print("Your number is NOT divisible by 3 and is divisible by 5.")
    else:
        print("Your number is NOT divisible by 3 and 5.")