#Day 5 Project: Password Generator.
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Welcome to the Password Generator.

password_caracteres = []

# Random letters
qnt_letters = int(input("How many letters would you like in your password?\n"))

for letters_loop in range(1, qnt_letters + 1):
    random_letters = str(letters[random.randint(0, int(len(letters)) - 1)])
    password_caracteres.extend([random_letters]) 
    
# Random symbols
qnt_symbols = int(input("How many symbols would you like?\n"))

for symbols_loop in range(1, qnt_symbols + 1):
    random_symbols = str(symbols[random.randint(0, int(len(symbols)) - 1)])
    password_caracteres.extend ([random_symbols])

# Random numbers
qnt_numbers = int(input("How many numbers would you like?\n"))

for numbers_loop in range(1, qnt_numbers + 1):
    random_numbers = str(numbers[random.randint(0, int(len(numbers)) - 1)])
    password_caracteres.extend ([random_numbers])

 # Password caracteres and shuffle.
random.shuffle(password_caracteres)

# Final password: 
final_password = ""
n_letter = 0

for password_as_string in range(1, len(password_caracteres) + 1):
    final_password += password_caracteres[n_letter]
    n_letter += 1


print(f"Here is your password: {final_password}") 







