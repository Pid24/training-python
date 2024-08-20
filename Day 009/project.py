import os

def clear_console():
    # Clears the console for better user experience
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

def bidding_system():
    print("""
                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
    """)

    bidders = {}
    bidding_finished = False

    while not bidding_finished:
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        bidders[name] = bid

        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if should_continue.lower() == 'no':
            bidding_finished = True
            find_highest_bidder(bidders)
        elif should_continue.lower() == 'yes':
            clear_console()

if __name__ == "__main__":
    bidding_system()
