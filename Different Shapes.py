from turtle import Turtle, Screen
from random import random

tim = Turtle()
color_chosen = [0, 0, 0]
i = 3
tim.speed(0.7)
for i in range(3,11):
    for j in range(3):
        color_chosen[j] = random()
    tim.color(color_chosen)
    tim.pencolor(color_chosen)
    angle = 360/i
    for _ in range(0, i):
        tim.forward(100)
        tim.right(angle)

screen = Screen()
screen.exitonclick()


