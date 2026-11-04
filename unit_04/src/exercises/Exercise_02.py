
# Place your answer to Exercise_02 in this file
# Do not rename or remove this file

speed = int(input("What is the speed of the vehicle in mph?\n"))
hours = int(input("How many hours has it travelled?\n"))

if (hours<0):
    print("ERROR: Hours travelled must be a positive number.")
elif (speed<0):
    print("ERROR: Speed must be a positive number.")
else:
    print("Hour | Distance Travelled")
    print("-----------------------")
    for x in range (0,hours):
        print(f"{x+1}    | {speed * (x+1)}")
