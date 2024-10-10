from turtle import Screen, Turtle
from random import *

MOV_Y = 50
X_POSN_RIGHT = 350
X_POSN_LEFT = -350


class ScreenSetUp:
    def __init__(self):
        self.obj = Screen()
        self.pt_right = Turtle()
        self.pt_left = Turtle()
        self.set_screen()
        self.set_right_and_left_paddle()
        self.set_keybindings()

    def set_right_and_left_paddle(self):
        self.paddle(self.pt_right, X_POSN_RIGHT)
        self.paddle(self.pt_left, X_POSN_LEFT)
        self.obj.update()

    def paddle(self, obj, x_posn):
        obj.speed("fastest")
        obj.penup()
        obj.goto(x_posn, 0)
        obj.shape("square")
        obj.color("white")
        obj.shapesize(stretch_wid=5, stretch_len=1, outline=1)

    def set_screen(self):
        self.obj.tracer(0)
        self.obj.setup(800, 600)
        self.obj.bgcolor("black")
        self.obj.title("Pong")
        self.obj.update()

    def set_keybindings(self):
        self.obj.listen()
        self.obj.onkeypress(self.mov_up_right, "Up")
        self.obj.onkeypress(self.mov_down_right, "Down")
        self.obj.onkeypress(self.mov_up_left, "w")
        self.obj.onkeypress(self.mov_down_left, "s")
        self.obj.update()

    def mov_up_right(self):
        if self.pt_right.ycor() < 250:
            self.pt_right.goto(self.pt_right.xcor(), self.pt_right.ycor() + MOV_Y)
        self.obj.update()

    def mov_down_right(self):
        if self.pt_right.ycor() > -250:
            self.pt_right.goto(self.pt_right.xcor(), self.pt_right.ycor() - MOV_Y)
        self.obj.update()

    def mov_up_left(self):
        if self.pt_left.ycor() < 250:
            self.pt_left.goto(self.pt_left.xcor(), self.pt_left.ycor() + MOV_Y)
        self.obj.update()

    def mov_down_left(self):
        if self.pt_left.ycor() > -250:
            self.pt_left.goto(self.pt_left.xcor(), self.pt_left.ycor() - MOV_Y)
        self.obj.update()
