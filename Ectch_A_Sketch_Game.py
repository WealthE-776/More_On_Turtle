import turtle as t

screen = t.Screen()

billy = t.Turtle()
billy.speed('fastest')


def move_forwards():
    billy.forward(15)


def move_backward():
    billy.backward(15)


def counter_clockwise():
    billy.left(10)
    billy.forward(15)


def clock_wise():
    billy.right(10)
    billy.forward(15)


def clear():
    billy.penup()
    billy.clear()
    billy.home()
    billy.pendown()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a',fun = clock_wise)
screen.onkey(key ='d', fun = counter_clockwise )
screen.onkey(key = 'c',fun = clear)

screen.exitonclick()
