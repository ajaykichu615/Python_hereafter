"""Objective:
The player tries to guess a randomly selected number within a limited number of attempts.
Game Flow:

1. Game Start:

Display a welcome message.
Set a predefined range for the number (e.g., 1 to 100).
Generate a random number within this range.
Set a maximum number of attempts (e.g., 7).

2. User Interaction:

Prompt the player to guess a number.
Validate the input to ensure it’s a number within the range.
Track the number of attempts.

3. Feedback Mechanism:
If the guess is too high, display "Too high! Try again."
If the guess is too low, display "Too low! Try again."
If the guess is correct, congratulate the player and display the number of attempts taken.

4. End Condition:
If the player guesses correctly, end the game.
If the player uses all attempts without guessing correctly, reveal the correct number.

5. Replay Option:
Ask the player if they want to play again.
If they choose "yes", restart the game.
If they choose "no", display a goodbye message and exit.
---
"""
import random

print("_______________WELCOME TO THE GAME________________")


def generate_number():
    rand = random.randint(1, 100)

    for attempt in range(7):
        num = input(f"Attempt {attempt + 1}: What's your guess? (1-100): ")

        if not num.isdigit() or int(num) < 1 or int(num) > 100:
            print("Invalid input! Please enter a number between 1-100.")
            continue

        num = int(num)

        if num == rand:
            print(f"Congrats! You guessed it right in {attempt + 1} attempts!")
            return

        print("Too high! Try again.") if num > rand else print("Too low! Try again.")
        print(f"Attempts left: {7 - (attempt + 1)}")

    print(f"Sorry you've exhausted all attempts. Correct answer was {rand}")


# Game loop
while True:
    print("\nThe system has generated a number between 1-100.")
    print(f"You have 7 attempts to guess it correctly.\n")
    generate_number()

    choice = input("\nWould you like to play again? (Y/N): ").upper()
    if choice == 'N':
        print("Thanks for playing! Goodbye!")
        break
    elif choice != 'Y':
        print("Invalid choice. Please enter Y or N.")