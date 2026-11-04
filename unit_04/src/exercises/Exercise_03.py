# Place your answer to Exercise_03 in this file
# Do not rename or remove this file

ended = False
count = []
while not ended:
    val = float(input("Please enter a number. Enter 0 to stop\n"))
    count.append(val)
    if (val==0):
        if count[0]==0:
            print("No numbers entered.")
            ended  = True
        else:
            print(f"The largest of the numbers entered is {max(x for x in count if x!=0)}")
            ended = True
    else:
        continue
