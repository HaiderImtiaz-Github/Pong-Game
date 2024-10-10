from turtle import Turtle

SCORE_POSN = [(-150, 260), (150, 260)]


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score_right = 0
        self.score_left = 0
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.draw_cen_line()
        self.goto(SCORE_POSN[0])
        self.write(f"Score : {self.score_left}", align="center", font=("Courier", 24, "bold"))
        self.goto(SCORE_POSN[1])
        self.write(f"Score : {self.score_right}", align="center", font=("Courier", 24, "bold"))

    def draw_cen_line(self):
        for _ in range(-300, 300, 40):
            self.goto(0, _)
            self.write("|", align="center", font=("Courier", 24, "bold"))
