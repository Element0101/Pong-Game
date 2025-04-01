from turtle import Turtle
START_POSITIONS = [(-600, 0), (600, 0)]


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def up(self):
        """Up movements"""
        new_y = self.ycor() + 35
        self.goto(self.xcor(), new_y)


    def down(self):
        """Down movements"""
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)






