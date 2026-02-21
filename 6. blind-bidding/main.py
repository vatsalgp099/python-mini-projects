print("Welcome to this Blind Auction!\n")

permission = True
bidders_data = {}

def winner(bidders_data):
    maxi = 0
    win = ""
    for bidder in bidders_data:
        if bidders_data[bidder] > maxi:
            maxi = bidders_data[bidder]
            win = bidder

    print(f"The winner is {win} with a bid of ₹ {maxi}")

while permission:

    name = input("What is your name? ")
    bid = int(input("What is your bid?: ₹ "))

    bidders_data[name] = bid

    more_bid = input("Are there any other bidders? Y or N ").lower()

    if more_bid == "y":
        permission = True
        print("\n" * 10)
    elif more_bid == "n":
        winner(bidders_data)
        permission = False
    else:
        print("Invalid input. Please try again.")
        permission = False



