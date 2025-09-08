import turtle
from turtle import *
t = Turtle()
print("test")
t.speed('fastest')
def square(sidelength):
    '''Draws a square of a
    given sidelength'''
    for i in range(4):
        forward(sidelength)
        right(90)

""" def square(sidelength):
    '''Draws a square of a
    given sidelength'''
    for i in range(4):
        forward(sidelength)
        right(90)
def addSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length)
        length = length +5 
        t.right(5)
addSquares(60) """

def star(x):
    for i in range(5):
        t.forward(x)
        t.left(144)

def many_stars():
    length = 25
    for i in range(60):
        star(length)
        t.right(5)
        length += 5

many_stars()
turtle.done()
