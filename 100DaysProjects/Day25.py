#Day 25 Project: US States Game
import csv
import pandas
import turtle


# Creating State name Class
class State_name(turtle.Turtle):
    def __init__(self, state_name, x_position, y_position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x_position, y_position)
        self.write(f"{state_name}", False, "center", ("Courier", 8, "normal"))
        

# Map and Screen configuration
screen = turtle.Screen()
screen.title("U.S States Game")
image = "Extra_Data/Data25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# Reading States Table
States_csv = pandas.read_csv("Extra_Data/Data25/50_states.csv")

States_list = States_csv["state"].to_list()


# Answer Prompt
Number_of_Guesses = 0
Correct_Guesses = []


while len(Correct_Guesses) < 50:
    answer_state = screen.textinput(title=f"{len(Correct_Guesses)}/50 Guess the State", prompt="What's another state's name?").lower()

    if answer_state == "exit":
        break

    for state in States_list:
        if answer_state == state.lower():
            if state not in Correct_Guesses:
                Correct_Guesses.append(state)
                coordenates = States_csv[States_csv.state == state]
                x = int(coordenates.x)
                y = int(coordenates.y)
                writing_state = State_name(state, x, y)


missing_answers = []
for state in States_list:
    if state not in Correct_Guesses:
        missing_answers.append(state)

Csv_missing_answers = pandas.DataFrame(missing_answers)

print(Csv_missing_answers)



