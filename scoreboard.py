from turtle import Turtle

# constants
ALIGNMENT = "center"
FONT = ("courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file="highscore_store.txt", mode="r") as file:
            contents = file.read()
        self.highscore = int(contents)
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font= FONT)
        self.hideturtle()

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def score_reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.store_highscore()
        self.update_scoreboard()

    def store_highscore(self):
        with open(file="highscore_store.txt", mode="w") as file:
            file.write(str(self.highscore))
