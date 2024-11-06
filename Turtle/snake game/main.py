import time
import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

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

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x , new_y)
    segments[0].forward(20)





screen.exitonclick()
