# # import turtle
# from turtle import Turtle, Screen
# timmy = Turtle()
#
# timmy.shape("turtle")
# timmy.color("cyan4")
# timmy.fd(100)
#
#
#
# my_screen = Screen()
# my_screen.exitonclick()
# print(my_screen.canvheight)

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squitle", "Bidoof"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"


print(table)