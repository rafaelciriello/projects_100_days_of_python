from random import randint
from guess_the_number_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess actual answer
def check_number(guess, number, turns):
    """Check guess against number. Returns number of turns remaining."""
    if guess < number:
        print("Too low.")
        return turns - 1
    elif guess > number:
        print("Too high.")
        return turns - 1
    else:
        print(f"You got it! The answer was {number}.")

#Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' ro 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    #Choosing a random number between 1 and 100
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)
    print(f"Pssst, the correct answer is {number}")

    #Let the user a guess number
    turns = set_difficulty()

    guess = 0
    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        turns = check_number(guess, number, turns)
        if turns == 0:
            print("You've run out of guess. You lose.")
            return
game()