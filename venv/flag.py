import turtle
import time

idde_t = turtle.Turtle()
idde_t.speed("slowest")
idde_t.pensize(10)
# idde_t.hide_pen()
# turtle.colormode(255)
col_arr = ["blue", "yellow", "red", "white", "orange"]


def box_1():
    for c in range(2):
        idde_t.forward(60)
        idde_t.left(90)
        idde_t.forward(250)
        idde_t.left(90)


def box_2():
    for c in range(2):
        idde_t.forward(60)
        idde_t.left(90)
        idde_t.forward(50)
        idde_t.left(90)


def flag():
    for x in range(0, 5):
        idde_t.penup()
        idde_t.goto(-175 + (x * 60), 0)
        idde_t.pendown()
        idde_t.color(col_arr[x])
        idde_t.begin_fill()
        idde_t.fillcolor(col_arr[x])
        box_1()
        idde_t.end_fill()

    idde_t.forward(60)
    # box_2()
    for r in range(5):
        idde_t.penup()
        idde_t.goto(125, 0 + (r * 50))
        idde_t.pendown()
        idde_t.color(col_arr[4 - r])
        idde_t.begin_fill()
        idde_t.fillcolor(col_arr[4 - r])
        box_2()
        idde_t.end_fill()


flag()

time.sleep(10)
