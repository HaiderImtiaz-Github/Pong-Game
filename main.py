import ball
from screen_setup import ScreenSetUp
from ball import Ball
import time
from score import *

# Create the screen and ball instances and set them up
my_screen = ScreenSetUp()
my_ball = Ball()
score_board = Score()
playing = True


def move_ball():
    global playing
    my_ball.ball_mov()
    if my_ball.distance(my_screen.pt_right) < 25 and my_ball.xcor() > 340 or my_ball.distance(
            my_screen.pt_left) < 25 and my_ball.xcor() < -340:
        my_ball.bounce_paddle()
    if my_ball.xcor() > 400:
        score_board.score_left += 1
        score_board.update_score()
        my_ball.reset_position()
        # if score_board.score_right > 9 or score_board.score_left > 9:

    if my_ball.xcor() < -400:
        score_board.score_right += 1
        score_board.update_score()
        my_ball.reset_position()
    my_screen.obj.update()
    my_screen.obj.ontimer(move_ball, 50)


move_ball()
# Keep the window open until it is closed by the user
my_screen.obj.exitonclick()
