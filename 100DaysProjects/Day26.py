#Day 26 Project: NATO Alphabet 

import pandas

repeat = True


phonetic_alphabet_csv =  pandas.read_csv("Extra_Data/Data26/nato_phonetic_alphabet.csv")

phonetic_alphabet_dict = {row.letter: row.code for (index, row) in phonetic_alphabet_csv.iterrows()}

while repeat:
    word = input("Enter a word: ").upper()
    word = [letter for letter in word]

    try:
        phonetic_alphabet = [phonetic_alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        repeat = False
        print(phonetic_alphabet)


