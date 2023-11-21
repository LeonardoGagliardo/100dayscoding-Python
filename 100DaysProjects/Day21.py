#Day 21 Project: Snake Game

from turtle import Screen, Turtle
from Day20 import Food, Scoreboard
import time

screen = Screen()
screen.setup(width=1800, height=900)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

final_tail = Turtle("square")
final_tail.color("white")
final_tail.penup()

food = Food()
score = Scoreboard()

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
    if full_snake[0].heading() == 180:
        pass
    else:
        full_snake[0].seth(0)

def up():
    if full_snake[0].heading() == 270:
        pass
    else:
        full_snake[0].seth(90)

def left():
    if full_snake[0].heading() == 0:
        pass
    else:
        full_snake[0].seth(180)

def down():
    if full_snake[0].heading() == 90:
        pass
    else:
        full_snake[0].seth(270)   


screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(up, "Up")
screen.onkey(down, "Down")

screen.listen()

# The Game
game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)

    for each_part in range(len(full_snake) - 1, 0, -1):
       x = full_snake[each_part - 1].xcor()
       y = full_snake[each_part - 1].ycor()
       full_snake[each_part].goto(x, y)
    full_snake[0].forward(21)

    # Counting Points
    if full_snake[0].distance(food) <= 16:
        food.refresh()
        new_tail()
        score.adding_points(False)
        
    # Detecting colision with walls
    if full_snake[0].xcor() > 882 or full_snake[0].xcor() < -903 or full_snake[0].ycor() > 444 or full_snake[0].ycor() < -441:
        score.adding_points(True)
        game_on = False 
        
    # Detecting colision with tail

    for snake_parts in full_snake[1:]:
        if full_snake[0].distance(snake_parts) < 10:
            score.adding_points(True)
            game_on = False
    

screen.exitonclick()
