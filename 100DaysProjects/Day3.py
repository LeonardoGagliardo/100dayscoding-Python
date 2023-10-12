#Day 3 Project: Choices Mini-Game.

print("Welcome to Choices.\nYour Mission is to get the best ending possible based on your choices. Good luck!")

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_________
*******************************************************************************''')

choice = input('''You're at a cross road. Where do you want to go? Type "left" or "right"\n''').lower()

if choice == "left":
    choice = input('''You found a forest\nWhat do you want to do? Type "enter the forest" or "keep walking"\n''').lower()
    if choice == "enter the forest":
        print("You got lost in the woods and never found a way home.\nBad Ending.")
    elif choice == "keep walking":
        choice = input('''You found a strange man how offers you a coin, what do you do? Type "accept the coin" or "keep walking"\n''').lower()
        if choice == "accept the coin":
            print("you accept the coin and found out that was really valuable. You sold in the market and became really rich!!\nGood Ending.")
        elif choice == "keep walking":
            print("You leave and got home safe. Nothing special.\nNeutral Ending")
        else:
            print("Invalid Command. Game over")
    else: 
        print("Invalid Command. Game over")
        
        
elif choice == "right":
    choice = input('''You find a really creepy mansion, what do you want to do? Type "enter" or "keep walking"\n''').lower()
    if choice == "keep walking":
        print("You leave and got home safe. Nothing special.\n Neutral Ending")
    elif choice == "enter":
        choice = input('''Inside the mansion, you find three doors, one red, one yellow and one blue. Which one do you want to open? Type "red", "yellow" or "blue".\n''').lower()
        if choice == "red":
            print("You found a room full of treasures. You became really rich!!\nGood Ending.")
        elif choice == "yellow":
            print("You got transported to your bed. It was all a dream.\nNeutral Ending")
        elif choice == "blue":
            print("You open the door and found a small black hole. You got suck into it and disappear from time and space.\nBad Ending.")
        else:
            print("Invalid Command. Game over")
    else: 
        print("Invalid Command. Game over")   
else:
    print("Invalid Command. Game over")




            
