#hangman
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"Psssst, {chosen_word}")

display = []
for letter in chosen_word:
    display.append("_")

lives = 6
end_the_game = False

while not end_the_game:
    print(stages[lives])
    print(" ".join(display))

    guess = input("Guess a letter: ").lower()

    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in display:
        lives -= 1

    if lives == 0:
        print(stages[lives])
        print("You lose!")
        end_the_game = True

    if "_" not in display:
        end_the_game = True
        print("You win!")
        print("".join(display))
