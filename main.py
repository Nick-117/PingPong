import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")

screen.tracer(False)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()



# ball.shape("circle")
# ball.color("white")
# ball.shapesize(stretch_wid=1, stretch_len=1)
# ball.goto(0, 0)


screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)


game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)



    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()



    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()



    if ball.xcor() > 410:
        ball.reset_position()
        ball.move_right()
        scoreboard.l_point()




    if ball.xcor() < -410:
        ball.reset_position()
        ball.move_left()
        scoreboard.r_point()








screen.exitonclick()