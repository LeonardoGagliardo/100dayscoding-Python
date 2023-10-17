#Day 7 Project: Hangman game.
import random

# Images
hangman6 = '''
+---+
  |   |
      |
      |
      |
      |
=========
'''
hangman5 = '''
+---+
  |   |
  O   |
      |
      |
      |
=========
'''
hangman4 = '''
+---+
  |   |
  O   |
  |   |
      |
      |
=========
'''
hangman3 = '''
+---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''
hangman2 = '''
+---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''
hangman1 = '''
+---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''
hangman0 = '''
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''

#Player lifes
lifes = 6

def hangman():
    if lifes == 6:
      print(hangman6)
    elif lifes == 5:
       print(hangman5)
    elif lifes == 4:
       print(hangman4)
    elif lifes == 3:
       print(hangman3)
    elif lifes == 2:
       print(hangman2)
    elif lifes == 1:
       print(hangman1)
    else:
       print(hangman0)


#Welcoming

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
''')


#Preparing the game
word_list = ["camel", "hospital", "water", "house", "alligator", "wood", "door", "party", "dragon"]
chosen_word = random.choice(word_list)
letters_already_choosen = []
player_word = []

for number_of_underscores in range (len(chosen_word)):
    player_word.append("_")

hangman()
print(player_word)

# Players choice


while "_" in player_word and lifes > 0:

  guess_letter = input("\nGuess a letter:  ").lower()
  letter_position = -1

  if guess_letter in letters_already_choosen:
      print(player_word)
      print("\nYou have already choosen this letter, try another one")
      print(f"\nChoosen letters:{letters_already_choosen}")

  if guess_letter not in letters_already_choosen:
    letters_already_choosen.append(guess_letter)

    if guess_letter in chosen_word:
      for checking_letters in range (len(chosen_word)):
        letter_position += 1
        if chosen_word[letter_position] == guess_letter:
          player_word[letter_position] = guess_letter
      hangman()
      print(f"\nChoosen letters:{letters_already_choosen}")
      print(player_word)

    else:
        lifes -= 1
        hangman()
        print(player_word)
        print(f"\nThe letter {guess_letter} is not in the word. You Lost 1 life")
        print(f"Choosen letters:{letters_already_choosen}")
  

# Final result

if lifes > 0:
  print("\nCongratulations. You completed the word.\nYou win!!")
else:
  print(f"\nThe word was: {chosen_word}\nYou have lost all your lifes.\nYou lose :(")


























