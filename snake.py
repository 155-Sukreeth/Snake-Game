from turtle import Turtle
# constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments =[]
        self.create_snake()
        # head can only be declared after we create a list called segments,
        # and only after creating our snake, as the list would be empty and segments[0] won't be defined by then
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_segment(position)

    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[len(self.segments)-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

