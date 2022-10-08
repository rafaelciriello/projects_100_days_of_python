#blackjack
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

#Create a deal_card() function that uses the List below to *return* a random card.
def deal_card():
    '''uses the list to return a random card'''
    card = random.choice(cards)
    return card

#Deal the user and computer 2 cards each using deal_card() and append().
for number in range(0, 2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

#Create a function called calculate_score() that takes a List of cards as input and return the score.
def calculate_score():
    return sum()
