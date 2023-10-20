#Day 9 Project: Auction


print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\ 
                       .-------------.
                      /_______________\ \n\n''')



bidder = {}
add_bidder = "yes"

while add_bidder == "yes":

  name = input("What is your name?: ")
  bid = input("What's your bid?: $")
  bidder[name] = bid

#Adding more bidder's
  add_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  
  while not (add_bidder == "yes" or add_bidder == "no"):
    add_bidder = input("invalid command, please digit 'yes' or 'no'").lower()
    
#Final result
winner_bid = 0
winner = ""
for bidder_key in bidder:
  bidder_bid = int(bidder[bidder_key])
  if winner_bid < bidder_bid:
    winner_bid = bidder_bid
    winner = bidder_key
 
print(f"The winner is {winner} with a bid of ${winner_bid}")
    
      
      

