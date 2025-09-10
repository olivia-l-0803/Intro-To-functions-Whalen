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
  
def square(length):
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
   
def squareSpiral(irange):
    size = 5
    for i in range(irange):
        square(size)
        size += 15
        t.right(5)

squareSpiral(60)

for i in range(4):
    t.forward(100)
    t.left(90)