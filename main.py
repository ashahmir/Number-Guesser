import random
from art import logo
print(logo)
print("Welcome To The Number Guessing Game")
print("I have a number in my mind between 1 and 100.")


def select_difficulty():
    difficulty = input("Choose the level of Difficulty to Guess: Type 'easy', 'medium' or 'hard\n").lower()
    if difficulty == 'easy':
        return 10
    elif difficulty == 'medium':
        return 7
    elif difficulty == 'hard':
        return 5
    else:
        print("Invalid Input")
        return 0


lives = select_difficulty()
number = random.randint(1,100)

while lives > 0:
    print(f"You have {lives} attempts remaining to guess my number.")
    user_num = int(input("Enter Your Guess: "))
    if user_num > number:
        print("Too High")
    elif user_num < number:
        print("Too Low")
    else:
        lives = 0
        print(f"Congrats, You guessed the number {number}!!")
    lives -= 1

if lives == 0:
    print("You have used all your attempts, and couldn't guess the number, You Lost :(")
