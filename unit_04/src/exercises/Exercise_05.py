# Place your answer to Exercise_05 in this file
# Do not rename or remove this file

# The Number Guessing Game 
import random

# randomly generate a number between 1 and 10
#secret_guess = random.randint(1,10)
secret_guess = 3
guess_count = 0

print("Welcome to the Number Guessing Game!")
print("You need to try and guess the number between 1 and 10...")
print("If you wish to exit the game enter 0...")

guess = int(input("Please enter a guess:\n"))
if guess == secret_guess:
    print(f"Well done the correct answer was {secret_guess}")
    print("You took 1 guess")
else:
    while guess != secret_guess:
        if guess == 0:
            print(f"Program exited. The correct answer is {secret_guess}")
            break
        else:
            if guess < secret_guess:
                print("Your guess is too low, please try again.")
            elif guess > secret_guess:
                print("Your guess is too high, please try again.")
            guess = int(input("Please enter a guess:\n"))
            guess_count +=1
            
    print(f"Well done the correct answer was {secret_guess}")
    print(f"You took {guess_count+1} guesses")