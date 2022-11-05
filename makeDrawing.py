import numpy as np
from colorthief import ColorThief
import pandas as pd
from cmu_112_graphics import *

# given {emotion: [(r1,g1,b1),(r2,g2,b2),(r3,b3,g3)]}

d = {'sad': [(120, 4, 153),(231, 2, 3),(150, 100, 2)]}

def returnHex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

def emotionToColor(dict,emotion):
    colors = dict[emotion]
    hexValues = []
    for color in colors:
        r,g,b = color
        hexValues.append(returnHex(r,g,b))
    return hexValues

## --------DRAWING---------
userInput = input('emotion? ')

def appStarted(app):
    app.r = 4
    app.dots = []
    app.timerDelay = 1
    app.colors = emotionToColor(d,userInput)
    app.sqSize = app.height/10
    app.margin = 10
    app.color = app.colors[0]

def mouseDragged(app, event):
    cx, cy, color = event.x, event.y, app.color
    app.dots.append((cx,cy, color))

def mousePressed(app, event):
    if app.width - app.margin - app.sqSize <= event.x <= app.width - app.margin:
        if app.margin <= event.y <= app.margin + app.sqSize:
            app.color = app.colors[0]
        elif app.margin + app.sqSize <= event.y <= app.margin + 2*app.sqSize:
            app.color = app.colors[1]
        elif app.margin + 2*app.sqSize <= event.y <= app.margin + 3*app.sqSize:
            app.color = app.colors[2]
    else: pass

def getColorCoords(app, colorNum):
    x0 = app.width - app.margin - app.sqSize
    x1 = app.width - app.margin
    if colorNum==0:
        y0 = app.margin
        y1 = app.margin + app.sqSize
    elif colorNum==1:
        y0 = app.margin + app.sqSize
        y1 = app.margin + 2*app.sqSize
    else:
        y0 = app.margin + 2*app.sqSize
        y1 = app.margin + 3*app.sqSize
    return x0,y0,x1,y1

# draws boxes with possible colors
def drawColors(app, canvas):
    for i in range(len(app.colors)):
        x0,y0,x1,y1 = getColorCoords(app,i)
        canvas.create_rectangle(x0,y0,x1,y1,fill=app.colors[i])

# draws a single dot with the color attributed to the image
def drawDot(app, canvas, cx, cy, color):
    canvas.create_rectangle(cx-app.r,cy-app.r,cx+app.r,cy+app.r,
                           fill=color,outline=color)

def redrawAll(app, canvas):
    for dot in app.dots:
        cx, cy, color = dot
        drawDot(app, canvas, cx, cy, color)
    drawColors(app, canvas)

runApp(width=400,height=400)