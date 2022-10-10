import random
from guess_the_number_art import logo

print(logo)
print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
print(f"Pssst, th correct answer is {number}")

difficulty = input("Choose a difficulty. Type 'easy' ro 'hard': ")
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5
print(attempts)