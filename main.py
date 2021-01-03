# Eric Reece - 1/3/2021
# This is a simple guessing game written in python.
# Utilizes the random library to generate a random number between user-specified boundaries.
# If user guess is too high or too low, promptly displays said information.
import random

if __name__ == '__main__':
    print("Welcome to a basic guessing game!\n")
    user_guessing = True
    boundaries_set = False
    low_num = None
    high_num = None
    random_number = None
    while user_guessing:

        if not boundaries_set:
            # Obtain user boundaries to guess between
            try:
                low_num = int(input("Pick low boundary for the generator: "))
                high_num = int(input("Pick high boundary for the generator: "))
                random_number = random.randint(low_num, high_num)
            except ValueError:
                print("Please enter only integers.")

            boundaries_set = True
            # Generate random number between user boundaries
        # print("My secret number is:",random_number)
        # Obtain user guess
        guess = int(input("Guess a number between " + str(low_num) + " and " + str(high_num) + ":\n"))
        if guess is not random_number:
            if guess > random_number:
                print("Too high!")
            elif guess < random_number:
                print("Too low!")
        else:
            user_guessing = False
            user_choice = input("\n********\nYou win!\n********\nPlay again? [y/n]")
            if user_choice == 'y':
                boundaries_set = False
                user_guessing = True
            elif user_choice == 'n':
                print("Good bye.")
            else:
                print("Please enter either (y) or (n):\n")
