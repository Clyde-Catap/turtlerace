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
        tortoise.speed("slowest")
        tortoise.color(colors[color_number])
        tortoise.penup()
        tortoise.goto(x=-230, y=(location_y + 50))
        location_y += 50
        color_number += 1
        tortle_pen.append(tortoise)

spawner(4)


finish = False


def runn(racer):
    global finish
    while finish == False:
        racer.fd(random.randint(10,100))
        if racer.xcor() > 0:
            print(f"Winnter is {racer.color()[0]}")
            finish = True


#
# for fxn in tortle_pen:
#     f = runn(fxn)
#     racers.append(f)


# thread1 = threading.Thread(target=runn(tortle_pen[0]))
# thread2 = threading.Thread(target=runn(tortle_pen[1]))
# thread3 = threading.Thread(target=runn(tortle_pen[2]))
# thread4 = threading.Thread(target=runn(tortle_pen[3]))
#
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
#
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()













screen.exitonclick()

