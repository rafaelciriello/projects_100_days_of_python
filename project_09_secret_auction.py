#secret_auction

from secret_auction_art import logo
print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name? ")
    price = input("What's your bide? $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        bidding_finished = True

print(bids)
