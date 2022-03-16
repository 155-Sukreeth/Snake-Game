from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# we will turn off the animations of our snake's movement as it will look weird
screen.tracer(0)

# create a snake
freddy = Snake()
lunch = Food()
score = Scoreboard()

# controls for your game
screen.listen()
screen.onkey(freddy.move_up, "Up")
screen.onkey(freddy.move_down, "Down")
screen.onkey(freddy.move_left, "Left")
screen.onkey(freddy.move_right, "Right")

game_is_on = True
while game_is_on:
    # now we will refresh the screen to show our snake's final location/state
    screen.update()
    time.sleep(0.1)

    freddy.move()
    if freddy.head.distance(lunch) <= 20:
        lunch.refresh()
        freddy.extend()
        score.increase_score()

    # detect collision with wall
    if freddy.head.xcor() >= 300 or freddy.head.xcor() <= -300 or freddy.head.ycor() >= 300 or freddy.head.ycor() <= -300:
        game_is_on = False
        score.game_ended()

    # detect collision with tail
    for seg in freddy.segments:
        if seg == freddy.head:
            pass
        elif freddy.head.distance(seg) < 10:
            game_is_on = False
            score.game_ended()

screen.exitonclick()
