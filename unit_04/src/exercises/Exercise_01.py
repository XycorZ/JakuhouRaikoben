# Place your answer to Exercise_01 in this file
# Do not rename or remove this file

ended = False
avg = 0
count = 0
while not ended:
    val = float(input("Please enter a number. Enter 0 to stop\n"))
    if(val==0):
        if (avg ==0):
            print("No numbers entered.")
            break
        else:    
            print(f"The average of the numbers entered is {avg/count}")
            ended = True
    else:
        avg+=val
        count+=1
