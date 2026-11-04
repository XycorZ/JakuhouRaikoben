def num_digits(num:int):
    # remove the following line and write the function here
    digits = 0
    zero = False
    while not zero:
        if num>=1:
            num/=10
            digits+=1
        else:
            zero = True
            return digits


def main():
    # remove the following line and write your program here
    try:
        number = int(input("Please enter a positive whole number:\n"))
        if number <= 0:
            print("Invalid input.")
        else:
            if num_digits(number) == 1:
                print (f"{number} has {num_digits(number)} digit.")
            else:
                print (f"{number} has {num_digits(number)} digits.")
    except ValueError:
        print("Invalid input.")
    
    #print (f"{number} has {num_digits(number)}")

# This is needed for the tests. This is now the first bit of code Python will run.
if __name__ == "__main__":
    main() # calls the main function