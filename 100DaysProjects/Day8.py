#Day 7 Project: Ceasar Cipher.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text_input, shift_input):
    encode = ""
    
    if text_input != str:
        print("Please, only use letter's in the text")
    elif shift_input >= 27:
        print("The alphabet has only 26 letters. Please, use a shift smaller than 27")
    else:
        for text_letter_position in range(len(text_input)):
            encode_position = alphabet.index(text_input[text_letter_position]) + shift_input
            if encode_position > 25:
                encode_position -= 26
            encode += alphabet[encode_position]
        print(encode)


encrypt(text_input=text, shift_input=shift)





#Type 'encode' to encrypt, type 'decode' to decrypt:

#encode:
#Type your message:
#Type the shift number:
#Here's the encoded result:

#decode:
#Type your message:
#Type the shift number:

#Type 'yes' if you want to go again. Otherwise type 'no'.



#Se o número de shift passar de 25. Tenho que 