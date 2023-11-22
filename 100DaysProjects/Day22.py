#Day 22 Project: The Pong Game

from turtle import Turtle, Screen
import random
import time


# Screen setup

screen = Screen()
screen.setup(width= 1000, height= 700)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


# Classes

#Paddle class
class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.seth(90)
        self.shapesize(0.7, 3.5)
        self.speed(0)
        self.goto(x_position, 0)
        self.speed(3)

    def movement(self, Key_up, Key_down):

        def up():
            if self.ycor() < SCREEN_HEIGHT_Y - 60:
                self.seth(90)
                self.forward(35)

        def down():
            if self.ycor() > (SCREEN_HEIGHT_Y * -1) + 60:
                self.seth(270)
                self.forward(35)
        
        screen.onkey(up, Key_up)
        screen.onkey(down, Key_down)
        screen.listen()


#Ball class
class Ball(Turtle):
    def __init__(self, first_to_play):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        if first_to_play == 1:
            self.seth(random.randint(135, 225))
        elif first_to_play == 2:
            self.seth(random.choice([random.randint(0, 45), random.randint(315, 360)]))

    def change_direction(self):
        self.seth(self.heading() + random.randint(135, 225))

    def reset_ball(self):
        self.goto(0, 0)


#Scoreboard class

class Score(Turtle):
    def __init__(self, position_base_on_player):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position_base_on_player, SCREEN_HEIGHT_Y - 50)
        self.total_points = 0
        self.write(f"{self.total_points}", move=False, align="center", font=("Arial", 25,"normal"))

    def making_point(self, player_number):
        self.total_points += 1
        self.clear()
        self.write(f"{self.total_points}", move=False, align="center", font=("Arial", 25,"normal"))
        if self.total_points > score_to_win:
            self.goto(0, 0)
            self.write(f"  Game Over!!\nPlayer {player_number} Win!!", move=False, align="center", font=("Arial", 55,"normal"))
        
        
# Variables
SCREEN_WIDTH_X = 500
SCREEN_HEIGHT_Y = 340

paddle_1 = Paddle((SCREEN_WIDTH_X * -1) + 25)
paddle_2 = Paddle(SCREEN_WIDTH_X - 25)

player_turn = random.randint(1, 2)

ball = Ball(first_to_play = player_turn)

score_to_win = 3
score_paddle_1 = Score(-80)
score_paddle_2 = Score(80)

game_on = True

# Making the field lines
field_lines = Turtle()
field_lines.color("white")
field_lines.penup()
field_lines.goto(SCREEN_WIDTH_X * -1, SCREEN_HEIGHT_Y * -1)
field_lines.pendown()
field_lines.goto(SCREEN_WIDTH_X, SCREEN_HEIGHT_Y * -1)
field_lines.penup()
field_lines.goto(SCREEN_WIDTH_X * -1, SCREEN_HEIGHT_Y)
field_lines.pendown()
field_lines.goto(SCREEN_WIDTH_X, SCREEN_HEIGHT_Y)
field_lines.penup()
field_lines.goto(0, SCREEN_HEIGHT_Y * -1)
field_lines.pendown()
field_lines.hideturtle()

while field_lines.ycor() < SCREEN_HEIGHT_Y:
    field_lines.pensize(6)
    field_lines.seth(90)
    field_lines.forward(10)
    field_lines.penup()
    field_lines.forward(20)
    field_lines.pendown()



# Paddles movement 
paddle_1.movement("w", "s")
paddle_2.movement("Up", "Down")

screen.listen()


while game_on:
    screen.update()
    time.sleep(0.01)
    ball.forward(5)


    # Colision Ball with players
    if ball.distance(paddle_1) < 35 or ball.distance(paddle_2) < 35:
        ball.change_direction()


    # Colision Ball with Wall

    if ball.heading() > 90 and ball.heading() < 270:
        if ball.ycor() >= SCREEN_HEIGHT_Y - 4:
            ball.seth(ball.heading() + 90) 
        elif ball.ycor() <= (SCREEN_HEIGHT_Y * -1) + 4:
            ball.seth(ball.heading() - 90) 
        
    else:
        if ball.ycor() >= SCREEN_HEIGHT_Y - 4:
            ball.seth(ball.heading() - 90) 
        elif ball.ycor() <= (SCREEN_HEIGHT_Y * -1) + 4:
            ball.seth(ball.heading() + 90) 

    # Ball reset
    if ball.xcor() > SCREEN_WIDTH_X + 10 or ball.xcor() < (SCREEN_WIDTH_X * -1) - 10:

        if ball.xcor() > SCREEN_WIDTH_X:
            player_turn = 1
            score_paddle_1.making_point(1)
            
        else:
            player_turn = 2
            score_paddle_2.making_point(2)

        ball.clear()
        ball = Ball(player_turn)
        screen.update()
        time.sleep(1)

    # Game End
    if score_paddle_1.total_points > score_to_win or score_paddle_2.total_points > score_to_win:
        game_on = False
        

screen.exitonclick()


# Debungging
# Bola ao colidir na parede em um certo angulo, fica em um loop infinito (bate duas vezes) 
# Preciso deletar as bolas que saem do campo
# Winner Warning is reverse
# Colocar na frente da pontuação o jogador


