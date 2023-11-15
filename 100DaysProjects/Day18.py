#Day 18 Project: Hirst Painting

from turtle import Turtle, Screen
import colorgram
import random
import turtle


hirst = Turtle()
hirst.shape()
hirst.color("black")
turtle.colormode(255)


# Collecting the colors from a hirst painting
hirst_colors_list = []
colors = colorgram.extract('Extra_Data/Data18/hirst_painting.webp', 30)
for rgb_in_colors in colors:
    r = rgb_in_colors.rgb.r
    g = rgb_in_colors.rgb.g
    b = rgb_in_colors.rgb.b
    color_tuple = (r, g, b)
    hirst_colors_list.append(color_tuple) 


# Making the painting
hirst_height = -300
hirst.penup()
hirst.setpos(-250, hirst_height)

for line in range(10):
    hirst.speed(0)
    hirst.setpos(-250, hirst_height)
    hirst_height += 50
    for row in range (10):
        hirst.speed(8)
        dot_color = random.choice(hirst_colors_list)
        hirst.dot(25, dot_color)
        hirst.forward(62)


screen = Screen()
screen.exitonclick()




