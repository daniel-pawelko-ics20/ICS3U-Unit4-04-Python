#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Dec 2021
# For Loops

from random import randint


def main():
    # main function for creating for loop program

    # creating random number
    random_num = randint(0, 9)

    # process/output
    while True:
        guess = input("What is your guess: ")
        guess = int(guess)
        if guess == random_num:
            print(f"You guessed CORRECT, the number is {random_num}")
            break
        print("Incorrect :(")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
