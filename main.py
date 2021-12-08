#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Dec 2021
# Better Guessing Game

from random import randint


def main():
    # main function for creating guessing game

    # creating random number
    RANDOM_NUM = randint(0, 9)

    # process/output/input
    while True:
        guess = input("What is your guess: ")
        guess = int(guess)
        if guess == RANDOM_NUM:
            print(f"You guessed CORRECT, the number is {RANDOM_NUM}")
            break
        print("Incorrect :(")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
