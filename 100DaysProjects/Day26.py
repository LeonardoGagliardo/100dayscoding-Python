#Day 26 Project: NATO Alphabet 

import pandas

phonetic_alphabet_csv =  pandas.read_csv("Extra_Data/Data26/nato_phonetic_alphabet.csv")

phonetic_alphabet_dict = {row.letter: row.code for (index, row) in phonetic_alphabet_csv.iterrows()}

word = input("Enter a word: ").upper()
word = [letter for letter in word]

phonetic_alphabet = [phonetic_alphabet_dict[letter] for letter in word]

print(phonetic_alphabet)