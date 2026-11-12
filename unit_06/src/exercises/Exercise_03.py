def main():
    items_list = []
    ended=False
    while not ended:
        if len(items_list) != 10:
            numba = input("Please enter the next number: ")

            if numba != "q":
                items_list.append(int(numba))

            else:
                if numba == "q" and len(items_list)==0:
                    print("No numbers entered.")
                    ended=True

                elif numba =="q":
                    print("The reverse of the numbers entered is:")
                    for x in reversed(items_list):
                        print (x)
                    ended=True
        else:
            print("The reverse of the numbers entered is:")
            for x in reversed(items_list):
                print (x)
            ended = True

# This is the entry point of the program
if __name__ == "__main__":
    main()  # call the main function