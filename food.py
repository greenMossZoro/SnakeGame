from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        #will make the size of the circle half its original size
        #original size is 20 will change to 10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    
    def refresh(self):
        random_x = random.randint(-330, 330)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)