#blackjack
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_cards = []
user_cards = []

#selecting two random initial cards
for number in range(0, 2):
    computer_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))

print(f"The first card in the computer is: {computer_cards[0]}")
print(f"The first card in the user is: {user_cards[0]}")

#adding up the value of the cards
total_computer = sum(computer_cards)
total_user = sum(user_cards)

print(total_computer, total_user)

#check that the result is equal to 21
if total_computer == 21:
    print("You lose")
elif total_user == 21:
    print("you win")