from turtle import Screen, Turtle
from paddle import Paddle


LEFT_POSITION = (-350, 0)
RIGHT_POSITION = (350, 0)


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Creating a paddle
r_paddle = Paddle(RIGHT_POSITION)
l_paddle = Paddle(LEFT_POSITION)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()












screen.exitonclick()