from turtle import Turtle, Screen
import random
import threading
import multiprocessing


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which enter will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]



location_y = -200
color_number = 0
tortle_pen = []
def spawner(number):
    global color_number
    global location_y
    for tortoise in range(number):
        tortoise = Turtle(shape="turtle")
        tortoise.speed("fastest")
        tortoise.color(colors[color_number])
        tortoise.penup()
        tortoise.goto(x=-230, y=(location_y + 50))
        location_y += 50
        color_number += 1
        tortle_pen.append(tortoise)

spawner(6)


finish = False
#
#
# def runn(racer):
#     global finish
while finish == False:
    for racer in tortle_pen:
        racer.fd(random.randint(0,10))
        if racer.xcor() > 250:
            print(f"Winnter is {racer.color()[0]}")
            x = racer.color()[0]
            finish = True
if x == user_bet:
    print("You WIN")
else:
    print("You LOSE")