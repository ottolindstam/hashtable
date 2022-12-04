#Bar chart with turtle from:
#http://interactivepython.org/runestone/static/thinkcspy/Functions/ATurtleBarChart.html

import turtle
import random

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

def barChart(data):
    maxheight = max(data)
    numbars = len(data)
    border = 10
    wn = turtle.Screen()             # Set up the window and its attributes
    wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
    wn.bgcolor("beige")
    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("black")
    tess.fillcolor("gray")
    tess.pensize(3)
    for a in data:
        drawBar(tess, a)
    wn.exitonclick()

def myhash(name):
    #return len(name)
    return hash(name)%30

def calculateData(namefile):
    data = [0]*30
    with open(namefile) as f:
        f.readline()
        for name in f:
            i = myhash(name.strip())
            data[i] += 1
    return data


def main():
    data = calculateData("slumpnamn30.txt")
    barChart(data)

main()


