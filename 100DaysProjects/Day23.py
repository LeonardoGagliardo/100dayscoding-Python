#Day 23 Project: Crossing Game

from turtle import Turtle, Screen
import time
import random


# CLASSES

# Player Class

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(Start_position)
        self.shape("turtle")
        self.seth(90)

    def player_movement(self):
        def move_up():
            self.goto(player.xcor(), player.ycor() + TURTLE_PACE)
        def move_down():
            self.goto(player.xcor(), player.ycor() - TURTLE_PACE)
        
        screen.onkeypress(move_up, "Up")
        screen.onkeypress(move_down, "Down")
        screen.listen()


# Car Class

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.seth(180)
        self.shapesize(1, 2)
        self.color(random.choice(car_colors))

    def car_spawn(self):
        self.goto(random.randint(530, 1000), random.randint(-280, 280))


# Scoreboard Class

class Text(Turtle):
    def __init__(self, option):
        super().__init__()
        self.penup()
        self.hideturtle()

        if option == 1:
            self.clear()
            self.goto(SCREEN_WIDTH_X_NEGATIVE + 65, SCREEN_WIDTH_Y - 40)
            self.write(f"Level {level_number}", False, "center", ("Courier", 20, "normal"))
        elif option == 2:
            self.write(f"Game Over", False, "center", ("Courier", 25, "normal"))

# Screen Configurations
screen = Screen()
screen.setup(width= 1000, height= 700)
screen.title("Crossing Game")
screen.tracer(0)

# Constants
SCREEN_WIDTH_X = 500
SCREEN_WIDTH_X_NEGATIVE = -500
SCREEN_WIDTH_Y = 350
SCREEN_WIDTH_Y_NEGATIVE = -350
TURTLE_PACE = 20
CAR_QNT = 10


# Variables
game_on = True

Start_position = (0, -320)

player = Player()
car_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_cars = []
car_speed = 10
level_number = 1
level = Text(1)

# Making the field

field_tracer = Turtle()
field_tracer.penup()
field_tracer.goto(-500, -290)
field_tracer.pendown()
field_tracer.goto(500, -290)
field_tracer.penup()
field_tracer.goto(-500, 300)
field_tracer.pendown()
field_tracer.shape("square")
field_tracer.shapesize(0.5, 0.5)
field_tracer.penup()
while field_tracer.xcor() < 500:
    field_tracer.color("black")
    field_tracer.goto(field_tracer.xcor(), field_tracer.ycor() - 10)
    field_tracer.stamp()
    field_tracer.goto(field_tracer.xcor() + 10, field_tracer.ycor())
    field_tracer.color("white")
    field_tracer.stamp()
    field_tracer.goto(field_tracer.xcor(), field_tracer.ycor() + 10)
    field_tracer.color("black")
    field_tracer.stamp()
    field_tracer.goto(field_tracer.xcor() + 10, field_tracer.ycor())
    field_tracer.color("white")
    


# Adding Cars

for adding_car in range(CAR_QNT):
    adding_car = Car()
    adding_car.car_spawn()
    all_cars.append(adding_car)


# Game Loop
player.player_movement()




while game_on:
    screen.update()
    time.sleep(0.1)


    # Player Progress        
    if player.ycor() >= 300:

        # Dificult rise
        level_number += 1
        level.clear()
        level = Text(1)


        car_speed += 10
        for adding_car in range(2):
            adding_car = Car()
            adding_car.car_spawn()
            all_cars.append(adding_car)

        # Player reset
        player.goto(Start_position)


    # Cars Configuration:
    for car in all_cars:

        #Car movement
        car.forward(car_speed)

        # Car Respawning
        if car.xcor() <= SCREEN_WIDTH_X_NEGATIVE - 30:
            car.car_spawn()

        # Car/Player Colision
        if player.distance(car.xcor(), car.ycor()) <= 29:
            Game_over_warning = Text(2)
            screen.update()
            game_on = False



screen.exitonclick()





