# Rock-Paper-Scissors Game
# CODSOFT Internship - Task 4

import random

print("===== ROCK-PAPER-SCISSORS GAME =====")

user_score = 0
computer_score = 0

while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice: ").lower()

    # Check valid input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Computer selects randomly
    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("\nYour choice:", user_choice)
    print("Computer's choice:", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("Result: It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("Result: You win!")
        user_score += 1

    else:
        print("Result: You lose!")
        computer_score += 1

    # Display score
    print("Score - You:", user_score, "| Computer:", computer_score)

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing!")
        print("Final Score - You:", user_score, "| Computer:", computer_score)
        break
