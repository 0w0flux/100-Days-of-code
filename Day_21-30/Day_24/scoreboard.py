from turtle import Turtle
import csv
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.hideturtle()
        self.highscore_file_read()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} \nHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.highscore_file_write(self.high_score)
            self.highscore_file_read()

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def highscore_file_write(self, value):
        with open("Day_24\\high_score.csv", mode="a") as file:
            data = str(value)
            writer = csv.writer(file)
            writer.writerow([data])

    def highscore_file_read(self):
        with open("Day_24\\high_score.csv", mode="r") as file:
            reader = csv.reader(file)
            self.high_score = max(
                int(row[0])
                for row in reader
                if row
            )

    
            