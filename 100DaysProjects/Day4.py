#Day 4 Project: Rock Paper Scissors.
import random 

#ASCII Arts
rock_ascii = '''
    ______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) '''

paper_ascii = '''
  _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________) '''

scissor_ascii = '''
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) '''

invalid_ascii = '''
8b,     ,d8  
 `Y8, ,8P'   
   )888(     
 ,d8" "8b,   
8P'     `Y8'''


# My play
player_choice = input("What do you choose? Rock, Paper or Scissor?\n").lower()


# Computers Play
computer_options = ["rock", "paper", "scissor"]
computer_choice = computer_options[random.randint(0, 2)]

# Both Choices
if player_choice == "rock":
    print(f"You chose {player_choice}\n{rock_ascii}\n")
elif player_choice == "paper":
    print(f"You chose {player_choice}\n{paper_ascii}\n")
elif player_choice == "scissor":
    print(f"You chose {player_choice}\n{scissor_ascii}\n")
else: print(f"You chose {player_choice} -That's a invalid command\n{invalid_ascii}\n")

if computer_choice == "rock":
    print(f"The computer chose {computer_choice}\n{rock_ascii}\n")
elif computer_choice == "paper":
    print(f"The computer chose {computer_choice}\n{paper_ascii}\n")
elif computer_choice == "scissor":
    print(f"The computer chose {computer_choice}\n{scissor_ascii}\n")


# Matching result / Final result
if player_choice == computer_choice:
    print("It's a Tie.")
elif (player_choice == "rock" and computer_choice == "paper") or (player_choice == "scissor" and computer_choice == "rock") or (player_choice == "paper" and computer_choice == "scissor"):
    print("You lose :(")
elif (player_choice == "paper" and computer_choice == "rock") or (player_choice == "rock" and computer_choice == "scissor") or (player_choice == "scissor" and computer_choice == "paper"):
    print("You won. Congratulations!")
else: 
    print(f"Error: Impossible to find a result")