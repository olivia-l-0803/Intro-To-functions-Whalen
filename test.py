import turtle
from turtle import *
t = Turtle()


t.shape('turtle')
t.speed = 0.001



def triangle(length):
    t.forward(length)
    t.right(120)
    t.forward(length)
    t.right(120)
    t.forward(length)
    t.right(120)
  
def square(length):
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)

triangle(100)

t.goto(0,0)

square(100)