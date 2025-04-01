#Project description: Pong Arcade Game using the turtle Modul
#From: FreedomOutlines
#Start: 02.03.2025, 13:00 Uhr
#End: 02.03.2025, 21:00 Uhr

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


#Adding and configuring a new Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game by FreedomOutLines")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


#Event listener
screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)


game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect when paddles miss the ball
    if ball.distance(r_paddle) > 50 and ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()

    if ball.distance(l_paddle) > 50 and ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()












screen.exitonclick()