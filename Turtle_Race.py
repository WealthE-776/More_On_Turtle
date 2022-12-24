from turtle import Turtle, Screen
import random
#
screen = Screen()
screen.bgcolor('green')
screen.setup(width=700, height=400)
still_racing = False

user_bet = screen.textinput(title='Place your bets', prompt='Which turtle would you like to bet on?')
all_turtles = []

colors = ['red', 'orange', 'yellow', 'pink', 'blue', 'purple']
y_coordinates = [-100, -50, 0, 50, 100, 150]

for t_index in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[t_index])
    new_turtle.penup()
    new_turtle.setposition(x=-340, y=y_coordinates[t_index])
    new_turtle.speed('fastest')

    all_turtles.append(new_turtle)

if user_bet:
    still_racing = True

while still_racing:
    for turtle in all_turtles:
        if turtle.xcor() > 330:
            still_racing = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You 've won,The {winning_color} turtle is the winner! ")


            else:
                print(f"You lose,The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()
