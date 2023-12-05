#Day 31 Project: Capstone
import tkinter
import pandas
import random

# Reading File
French_words_path = "Extra_Data/Data31/french_words.csv"

with open(French_words_path) as words_csv:
    words_csv = pandas.read_csv(words_csv)
    words_csv = pandas.DataFrame(words_csv)
    words_dict = words_csv.to_dict(orient="records")

# Picking a random word

translation = ""
def picking_new_french_word():
    global translation, flip_timer, random_french_word
    window.after_cancel(flip_timer)
    random_french_word = random.choice(words_dict)
    french_word = random_french_word["French"]
    translation = random_french_word["English"]
    canvas.itemconfig(canvas_image, image=CARD_FRONT_IMAGE)
    canvas.itemconfig(title_card, text="French", fill="black")
    canvas.itemconfig(word_card, text=f"{french_word}", fill="black")
    flip_timer = window.after(3000, func=flip_card)
    
    
def flip_card():
    canvas.itemconfig(canvas_image, image=CARD_BACK_IMAGE)
    canvas.itemconfig(title_card, text="English", fill="white")
    canvas.itemconfig(word_card, text=f"{translation}", fill="white")

def is_know():
    words_dict.remove(random_french_word)
    picking_new_french_word()
    


# Screen config

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 35, "italic")
WORD_FONT  = ("Arial", 60, "bold")

window = tkinter.Tk()
window.title("Capstone Project")
window.config(bg= BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)


# Images Paths 
RIGHT_IMAGE = tkinter.PhotoImage(file="Extra_Data/Data31/right.png")
WRONG_IMAGE = tkinter.PhotoImage(file="Extra_Data/Data31/wrong.png")
CARD_FRONT_IMAGE = tkinter.PhotoImage(file="Extra_Data/Data31/card_front.png")
CARD_BACK_IMAGE = tkinter.PhotoImage(file="Extra_Data/Data31/card_back.png")


# Card Config

canvas = tkinter.Canvas(width= 1000, height= 580, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(500, 313, image=CARD_FRONT_IMAGE)
title_card = canvas.create_text(500, 180, text="French", font=TITLE_FONT)
word_card =  canvas.create_text(500, 320, text=f"word", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)


# Button Config

right_button = tkinter.Button(image= RIGHT_IMAGE, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_know)
wrong_button = tkinter.Button(image=WRONG_IMAGE, highlightthickness=0, bg=BACKGROUND_COLOR, command=picking_new_french_word)

right_button.grid(column= 1, row=1)
wrong_button.grid(column= 0, row=1)


picking_new_french_word()


window.mainloop()

