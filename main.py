from turtle import Turtle, Screen

ally = Turtle()
screen = Screen()


def move_forwards():
    ally.forward(10)


screen.listen()
screen.onkey(key='space', fun=move_forwards)
screen.exitonclick()
