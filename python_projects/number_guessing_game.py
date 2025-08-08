"""Guess the number game."""
import random

LOW = 1
HIGH = 100


def main():
    target = random.randint(LOW, HIGH)
    print(f"Guess a number between {LOW} and {HIGH}")
    attempts = 0
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
        except ValueError:
            print("Enter a valid number")
            continue

        if guess < target:
            print("Too low")
        elif guess > target:
            print("Too high")
        else:
            print(f"Correct! You guessed it in {attempts} tries.")
            break

if __name__ == "__main__":
    main()
