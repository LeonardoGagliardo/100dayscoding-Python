#Day 20 Project: Snake Game Classes
from turtle import Screen, Turtle
import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 450

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()
       
        
        
    def refresh(self):
        random_x = random.randint((SCREEN_WIDTH * -1) + 100, SCREEN_WIDTH - 100)
        random_y = random.randint((SCREEN_HEIGHT * -1) + 100, SCREEN_HEIGHT - 100)
        self.goto(random_x, random_y)
        

    

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, SCREEN_HEIGHT - 50)
        self.total_points = 0
        self.write(f"Score = {self.total_points}", move=False, align="center", font=("Arial", 18,"normal"))

    def adding_points(self, game_over):
        self.clear()
        if game_over == False:
            self.total_points += 1
            self.write(f"Score = {self.total_points}", move=False, align="center", font=("Arial", 18,"normal"))
        else: 
            self.goto(0, 0)
            self.write(f"Game Over!\nYour Final Score is: {self.total_points}", move=False, align="center", font=("Arial", 25,"normal"))
        
    
    