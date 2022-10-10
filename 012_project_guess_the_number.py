import random
from guess_the_number_art import logo

print(logo)
print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
print(f"Pssst, the correct answer is {number}")

difficulty = input("Choose a difficulty. Type 'easy' ro 'hard': ").lower()
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

end_the_game = False
while not end_the_game:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts -= 1
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print(f"You got it! The answer was {number}.")
        end_the_game = True
    if attempts == 0:
        print("You have no more attempts.")
        end_the_game = True
