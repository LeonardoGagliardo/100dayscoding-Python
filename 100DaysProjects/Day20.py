#Day 20 Project: Snake Game

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


 
final_tail = Turtle("square")
final_tail.color("white")
final_tail.penup()

full_snake = [final_tail]

# Snake new tail
def new_tail():
    new_tail = Turtle("square")
    new_tail.color("white")
    new_tail.penup()
    new_tail.speed(0)
    global final_tail
    if final_tail.heading() == 0:
        new_tail.seth(0)
        new_tail.goto(final_tail.xcor() - 20, final_tail.ycor())
    elif final_tail.heading() == 90:
        new_tail.seth(90)
        new_tail.goto(final_tail.xcor(), final_tail.ycor() -20) 
    elif final_tail.heading() == 180:
        new_tail.seth(180)
        new_tail.goto(final_tail.xcor() + 20, final_tail.ycor())
    elif final_tail.heading() == 270:
        new_tail.seth(270)
        new_tail.goto(final_tail.xcor(), final_tail.ycor() + 20)
    final_tail = new_tail
    full_snake.append(final_tail)

new_tail()
new_tail()

# Key Presses
def right():
    full_snake[0].right(90)

def left():
    full_snake[0].left(90)

screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.listen()

# The Game
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    for each_part in range(len(full_snake) - 1, 0, -1):
       x = full_snake[each_part - 1].xcor()
       y = full_snake[each_part - 1].ycor()
       full_snake[each_part].goto(x, y)
       

    full_snake[0].forward(21)
        
    

screen.exitonclick()

