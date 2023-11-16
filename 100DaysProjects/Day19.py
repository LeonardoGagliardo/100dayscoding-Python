#Day 19 Project: Turtle Race

from turtle import Turtle, Screen 
import random

screen = Screen()
screen.setup(width=500, height=500)
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the race? Enter a color between\n(red, orange, yellow, green, blue, purple)")


colors= ["red", "orange", "yellow", "green", "blue", "purple"]

ted = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
timmy = Turtle(shape="turtle")
tiresse = Turtle(shape="turtle")
thomas = Turtle(shape="turtle")
tommy = Turtle(shape="turtle")

turtles = [ted, tom, timmy, tiresse, thomas, tommy]

x = -240
y = -200
color_position = 0
bet_table = {}
for setup_turtle in turtles:
    setup_turtle.color(colors[color_position])
    color_position += 1
    setup_turtle.penup()
    setup_turtle.goto(x, y)
    y += 81
    bet_table[setup_turtle] = colors[color_position - 1]

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_turn in turtles:
        random_distance = random.randint(0, 30)
        turtle_turn.forward(random_distance)
        if turtle_turn.xcor() >= 220:
            winner = bet_table[turtle_turn]
            print(f"The Winner is the color {winner}")
            is_race_on = False
        
if winner == user_bet:
    print("You Win")
else:
    print("Wrong bet. You lose")


screen.exitonclick()


