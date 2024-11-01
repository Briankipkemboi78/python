import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


circles = 72

for _ in range(circles):
    tim.pensize(2)
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + 5)



screen = Screen()
screen.exitonclick()

