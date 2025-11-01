from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
import food

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = food.Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.up,"w")

screen.onkey(snake.down,"Down")
screen.onkey(snake.down,"s")

screen.onkey(snake.left,"Left")
screen.onkey(snake.left,"a")

screen.onkey(snake.right,"Right")
screen.onkey(snake.right,"d")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # scoreboard.update_screen()

    snake.move()
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.snake_head.xcor()> 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False


    for i in snake.snake_list[1:]:
        if snake.snake_head.distance(i) < 10:
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()