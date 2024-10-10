import random
from turtle import Turtle

BALL_SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed_x = BALL_SPEED
        self.ball_speed_y = BALL_SPEED
        self.pong_ball()
        self.ball_start()

    def ball_start(self):
        self.setheading(random.randint(0, 360))

    def ball_mov(self):
        new_x_cord = self.xcor() + self.ball_speed_x
        new_y_cord = self.ycor() + self.ball_speed_y
        self.goto(new_x_cord, new_y_cord)

        # Bounce off the top and bottom walls
        if new_y_cord > 290 or new_y_cord < -290:
            self.bounce()

        # Bounce off the left and right walls
        # if new_x_cord > 390 or new_x_cord < -390:
        #     self.ball_speed_x *= -1

    def pong_ball(self):
        self.penup()
        self.color("white")
        self.shape("circle")

    def bounce(self):
        self.ball_speed_y *= -1

    def bounce_paddle(self):
        self.ball_speed_x *= -1
        self.ball_speed_x *= 1.1
        self.ball_speed_y *= 1.1

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed_x = BALL_SPEED
        self.ball_speed_y = BALL_SPEED
        self.ball_start()
