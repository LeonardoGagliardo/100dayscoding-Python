#Day 8 Project: Ceasar Cipher.
print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Encrypring Function
def encrypt(text_input, shift_input):
    encode = ""

    if shift_input >= 27:
        print("The alphabet has only 26 letters. Please, use a shift smaller than 27")

    else:
        for text_letter_position in range(len(text_input)):
            encode_position = alphabet.index(text_input[text_letter_position]) + shift_input
            if encode_position > 25:
                encode_position -= 26
            encode += alphabet[encode_position]
        print(f"The encoded text is: {encode}")

# Decrypting Function
def decrypt(text_input, shift_input):
    decode =""

    if shift_input >= 27:
        print("The alphabet has only 26 letters. Please, use a shift smaller than 27")

    else:
        for text_letter_position in range(len(text_input)):
            decode_position = alphabet.index(text_input[text_letter_position]) - shift_input
            if decode_position > 25:
                decode_position += 26
            decode += alphabet[decode_position]
        print(f"The decoded text is: {decode}")


if direction == "encode":
    encrypt(text_input=text, shift_input=shift)
elif direction == "decode":
    decrypt(text_input=text, shift_input=shift)
else:
    print("Invalid input")