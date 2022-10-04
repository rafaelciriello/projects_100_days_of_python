#secret_auction

from secret_auction_art import logo
bids = {}

def added_bid(user_name, user_bid):
    bids[user_name] = user_bid

print(logo)
print("Welcome to the secret auction program.")

end_the_action = False

while not end_the_action:
    user = input("What is your name? ")
    bid = input("What's your bide? $ ")
    new_user = input("New user? 'Y' or 'N': ").lower()

    if new_user == "n":
        end_the_action = True

    added_bid(user_name=user, user_bid=bid)

print(bids)