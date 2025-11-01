from turtle import Turtle
SNAKE_CORDINATE = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:


    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.snake_head = self.snake_list[0]


    def create_snake(self):
        for i in SNAKE_CORDINATE:
            self.add_snake(i)

    def add_snake(self,i):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.width(20)
        new_snake.goto(i)
        self.snake_list.append(new_snake)

    def extend(self):
        self.add_snake(self.snake_list[-1].position())

    def move(self):
        for num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[num - 1].xcor()
            new_y = self.snake_list[num - 1].ycor()
            self.snake_list[num].goto(new_x, new_y)
        self.snake_head.fd(MOVE_DISTANCE)


    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.seth(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.seth(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.seth(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.seth(RIGHT)
