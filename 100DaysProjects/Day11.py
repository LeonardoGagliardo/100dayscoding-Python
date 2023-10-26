#Day 11 Project: BlackJack 


print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = [ random.choice(cards), random.choice(cards)]
player_points = 0
dealer_hand = [random.choice(cards), random.choice(cards)]
dealer_points = 0


# Beginning of the game

def adding_points(x_hand, x_points):
    x_points = 0
    for card in x_hand:
        x_points += card
    return x_points

def converting_A(x_hand):
    for A in x_hand:
         if A == 11:
              x_hand[x_hand.index(11)] = 1
              

player_points = adding_points(player_hand, player_points)


game_loop = True
while game_loop:

    print(f"This is your hand: {player_hand}")
    print(f"This is the dealer hand: [{dealer_hand[0]}, ?]")

    if player_points == 21:
        game_loop = False
        print("Wow, you got 21 first hand, You win!")

    more_card = input("Do you want more cards? Choose 'y' or 'n'")

    if more_card == "y":
        player_hand.append(random.choice(cards))
        player_points = adding_points(player_hand, player_points)
        if player_points == 21:
            print(f"This is your hand: {player_hand}")
            print("You got BlackJack, you win!!")
            game_loop = False
        elif player_points > 21:
            converting_A(player_hand)
            player_points = adding_points(player_hand, player_points)
            if player_points == 21:
                print(f"This is your hand: {player_hand}")
                print("You got BlackJack, you win!!")
                game_loop = False
            elif player_points > 21:
                print(f"This is your hand: {player_hand}")
                print("You burst. You lose")
                game_loop = False

    elif more_card == "n":
        game_loop = False

#Final result

if not (player_points == 21 or player_points > 21):
    print(f"This is your final hand: {player_hand}")
    print(f"This is the dealer hand: {dealer_hand}")

    dealer_points = adding_points(dealer_hand, dealer_points)

    if dealer_points == 21:
        print("Ufh... the dealer got BlackJack, You lose.")
    elif dealer_points < 17:
        while dealer_points < 17:
            print("The dealer hits one more card")
            dealer_hand.append(random.choice(cards))
            print(f"This is your final hand: {player_hand}")
            print(f"This is the dealer hand: {dealer_hand}")
            dealer_points = adding_points(dealer_hand, dealer_points)
            if dealer_points > 21:
                converting_A(dealer_hand)
                dealer_points = adding_points(dealer_hand, dealer_points)

    if dealer_points > 21:
        print("The dealer bust! you win")
    else:
        if player_points > dealer_points:
            print(f"You got {player_points} points and the dealer {dealer_points}. You won!")
        else:
            print(f"You got {player_points} points and the dealer {dealer_points}. You lose...")

