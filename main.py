from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:

    segment = Turtle("square")
    segment.color("white")
    segment.goto(position)
    segment.append(segment)

game_is_on = True
while game_is_on:
    

screen.exitonclick()