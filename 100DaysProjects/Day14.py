#Day 14 Project: Higher or Lower Game

# Arts:

print( '''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
''' )

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

# Imports
from  Extra_Data.Data14.Data14 import data
import random


# The highet or lower game
def higher_or_lower_game():
    score = 0
    continuar = True

    while continuar:
        # Preparing Options
        optionA = random.choice (data)
        followersA = int(optionA['follower_count'])
        optionB = random.choice (data)
        followersB = int(optionB['follower_count'])

        while followersA == followersB:
            optionB = random.choice (data)
            followersB = int(optionB['follower_count'])

        # Showing Options
        player_choice = ""

        while not (player_choice == 'a' or player_choice == 'b'):
            print(f'Option A: {optionA['name']}, a {optionA['description']}, from {optionA['country']}')
            print(f'{vs}')
            print(f'Option B: {optionB['name']}, a {optionB['description']}, from {optionB['country']}')
            player_choice = input('\nWho was more followers? Type "A" or "B":  ').lower()
            print("\n")
            if not (player_choice == 'a' or player_choice =='b'):
                print('\nYou choose an invalid input, please try again\n') 
                
        # Resultado
        
        if player_choice == 'a':
            if followersA > followersB:
                score += 1
                print(f"You're right! Current score: {score}\n\n")
            else:
                continuar = False
                print(f"Sorry, that's wrong. Final score: {score}\n\n")
        elif player_choice == 'b':
            if followersB > followersA:
                score +=1
                print(f"You're right! Current score: {score}\n\n")
            else:
                continuar = False
                print(f"Sorry, that's wrong. Final score: {score}\n\n")

    play_again = input("Do you want to play again? press 'y' if you do.").lower()
    if play_again == 'y':
        higher_or_lower_game()


#calling the function for the first time
higher_or_lower_game()






