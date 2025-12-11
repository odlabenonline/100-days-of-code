from turtle import Turtle, Screen

timmy = Turtle()

# We could run the code below 4 times to get timmy to draw a square or use a for loop
for i in range(4):
    timmy.forward(100)
    timmy.left(90)

screen = Screen()
screen.exitonclick()
