from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    screen.resetscreen()


def anti_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=anti_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()
