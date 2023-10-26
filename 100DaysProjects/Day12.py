#Day 12 Project: The Number Guessing Game
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Try to Guess!!")


def guessing_game():
    """The guessing game function"""
    
    attempts = 0
    the_number = random.randint(1, 100)
    player_guess = 0

    not_valid = True
    while not_valid: 
        difficult = input("Choose a difficulty. Type 'easy' or 'hard'\n").lower()
        if difficult == "easy":
            attempts = 10
            not_valid = False
        elif difficult == "hard":
            attempts = 5
            not_valid = False
        else:
            print("Not a valid input") 
        
    print(f"Ok, you have {attempts} attempts.")

    while attempts > 0 and not player_guess == the_number :
        player_guess = int(input("Make a Guess: \n"))
        if player_guess > the_number:
            attempts -= 1
            print(f"Too high.\nYou have {attempts} attempts left")
        elif player_guess < the_number:
            attempts -=1
            print(f"Too low.\nYou have {attempts} attempts left")
        else:
            print(f"You got it! The answer was {the_number}.")

    if attempts == 0:
        print("You've run out of guesses, you lose.")

    
    not_valid = True
    while not_valid:
        restart = input("Do you want to play again? Type 'y' or 'n'").lower()
        if restart == "y":
            not_valid = False
            guessing_game()
        elif restart == "n":
            not_valid = False
        else:
            print("Not a valid input")

guessing_game()



