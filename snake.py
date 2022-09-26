from turtle import Screen, Turtle, position

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    #method creates the image of the snake game
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segments = Turtle("square")
        new_segments.penup()
        new_segments.color("white")
        new_segments.goto(position)
        self.segments.append(new_segments)
    

    #add a new segment to snake every time score increaments
    def extend(self):
        #we will add segments to the end of the list using index -1 to represent it
        self.add_segment(self.segments[-1].position())


    #method makes the snake move forward 20 paces
    def move(self):
        for i in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
    
        self.head.fd(MOVE_DISTANCE)

    #method allows snake to move up
    def up(self):
        #this stops the snake from backtracking directions
        if self.head.heading() != DOWN:
            self.head.setheading(UP) 

    #method allows snake to move down
    def down(self):
        #this stops the snake from backtracking directions
        if self.head.heading() != UP:
            self.head.setheading(DOWN) 

    #method allows snake to move left
    def left(self):
        #this stops the snake from backtracking directions
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT) 

    #method allows snake to move right
    def right(self):
        #this stops the snake from backtracking directions
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 

