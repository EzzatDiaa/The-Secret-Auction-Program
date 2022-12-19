print("Hello to the secret auction")
from secret_auction_files import logo
from secret_auction_files import clear
print(logo)

bidders = {}
bidding_finished = False

def highest_bidder(dic):
  highest_bid = 0
  winner = ""
  for bidder in dic:
    bid_amount = dic[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with bid of {highest_bid}$ is the highest")

while not bidding_finished:
  name = input("What is your name?: ").lower()
  bid = int(input("What is your bid?: $"))
  bidders[name] = bid
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
  if should_continue == "no":
    bidding_finished = True
    highest_bidder(bidders)
  elif should_continue == "yes":
    clear()




