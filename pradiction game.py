import random

def guess_number():
    print("Welcome to the Number Guessing Game!\n")
    answer = random.randint(1, 10)
    guess = 0
    tries = 0

    while guess != answer:
        guess = int(input("Guess a number between 1 and 10: "))
        tries += 1

        if guess < answer:
            print("Too low, try again.")
        elif guess > answer:
            print("Too high, try again.")

    print("\nCongratulations, you guessed the number in", tries, "tries!")

guess_number()