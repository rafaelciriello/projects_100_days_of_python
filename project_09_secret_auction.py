#secret_auction

from secret_auction_art import logo
print(logo)
print("Welcome to the secret auction program.")

bids = {}

name = input("What is your name? ")
price = input("What's your bide? $")
bids[name] = price

print(bids)
