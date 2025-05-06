# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)

data = {}
continue_bid = True

def highest_bidder(data):
    high_bid = 0
    winner = ''

    for user in data:
        bid = data[user]
        if bid > high_bid:
            high_bid = bid
            winner = user
    print(f"The winner is {winner} with a bid of ${high_bid}")


while continue_bid:
    user_input = input("What is your name? ")
    user_bid = int(input("Whats is your bid? "))
    data[user_input] = user_bid
    question = input("Any other bidders? Type 'yes' or 'no'.\n")

    if question == 'no':
        continue_bid = False
        highest_bidder(data)
    elif question == 'yes':
        print("\n" * 20)

