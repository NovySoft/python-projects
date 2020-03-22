import turtle 
from turtle import Turtle, Screen
import tkinter

screen = Screen()
t = Turtle("turtle")
t.speed(-1)

def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def clickright(x, y):
    t.clear()


def main():
    screen.listen()

    t.ondrag(dragging)

    screen.onscreenclick(clickright, 3)

    screen.mainloop()

main()
