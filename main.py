from art import logo
import os

bidder_log = {}

def check_winner(bidder_log):
  highest_bid = 0
  winner = ""

  for bidder in bidder_log:
    bid_value = bidder_log[bidder]
    if bid_value > highest_bid:
      highest_bid = bid_value
      winner = bidder

  print(f"The winner is {winner} with a bid of {highest_bid}")

print(logo)
should_stop = False

while not should_stop:
  bidder_name = input("What is your name?: ")
  bid_value = int(input("What is your bid?: $"))
  bidder_log[bidder_name] = bid_value
  next_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

  if next_bid == "no":
    should_stop = True
  elif next_bid == "yes":
    os.system("clear")
check_winner(bidder_log)
