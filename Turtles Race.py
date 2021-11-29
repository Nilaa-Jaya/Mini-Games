from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:  ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_axis = -125
for i in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=y_axis)
    y_axis += 50

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            race_is_on = False
            if turtle.color()[0] == user_bet:
                print(f"Congratulations! The {turtle.color()[0]} color turtle won")
            else:
                print(f"You lost, the {turtle.color()[0]} color turtle won")




