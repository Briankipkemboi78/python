import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position = [(-40, 0), (-20, 0), (0, 0)]

# Create turtles and position them on the screen
all_turtles = []
for position in starting_position:
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")  # Set color using hex code
    new_turtle.penup()
    new_turtle.goto(position)
    all_turtles.append(new_turtle)

screen.exitonclick()
