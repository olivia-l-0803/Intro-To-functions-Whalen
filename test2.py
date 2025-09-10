import turtle
from turtle import *
t = Turtle()

t.speed(20)
t.shape("turtle")

def square(length):
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
   
def squareSpiral(irange, size):
    for i in range(irange):
        t.right(5)
        square(size)
        size += 5
        
#squareSpiral(60, 10)

def star(libg):
    t.forward(libg)
    t.right(144)
    t.forward(libg)
    t.right(144)
    t.forward(libg)
    t.right(144)
    t.forward(libg)
    t.right(144)
    t.forward(libg)
    t.right(144)

def starSpiral(monkey, banana):
    for i in range(monkey):
        t.right(5)
        star(banana)
        banana += 5

#starSpiral(60, 6)

turtle.goto(0,0)

squareSpiral(100, 3)