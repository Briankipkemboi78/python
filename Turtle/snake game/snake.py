import time
import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_position = [(-40, 0), (-20, 0), (0, 0)]

# Create turtles and position them on the screen
segments = []
for position in starting_position:
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")  # Set color using hex code
    new_turtle.penup()
    new_turtle.goto(position)
    segments.append(new_turtle)

screen.update()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    for seg in segments:
        seg.forward(20)




screen.exitonclick()
