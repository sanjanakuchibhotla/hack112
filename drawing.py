from cmu_112_graphics import *

d = {'sad': [(120, 4, 153),(150, 27, 30),(150, 100, 2)]}

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
# initializes app values
def appStarted(app):
    app.r = 4
    app.dots = []
    app.timerDelay = 1
    app.colors = emotionToColor(d,userInput if userInput=='sad' else 'sad')
    app.sqSize = app.height/10
    app.margin = app.width/20
    app.color = app.colors[0]
    app.erasing = False
    app.slideY = app.height - app.margin
    app.slideX = app.width/4
    app.slideR = 5
    app.lineX = app.width/2
    app.lineY = app.height - app.margin

# actions when mouse is dragged
def mouseDragged(app, event):
    # erases dots at the mouse position
    if app.erasing:
        dot = clickedInDot(app, event.x, event.y)
        if dot: app.dots.remove(dot)
        if clickedOnSlider(app, event.x, event.y) and \
            .5*app.lineX <= event.x <= 1.5*app.lineX:
            if event.x > app.slideX: app.r += 0.5
            if event.x < app.slideX: app.r -= 0.5
            app.slideX = event.x
    # changes the radius based on slider position
    elif clickedOnSlider(app, event.x, event.y) and \
            .5*app.lineX <= event.x <= 1.5*app.lineX:
        if event.x > app.slideX: app.r += 0.5
        if event.x < app.slideX: app.r -= 0.5
        app.slideX = event.x
    # adds a dot at the mouse position to the list of dots
    else:
        if not clickedInSlideBox(app, event.x, event.y):
            cx, cy, color, r = event.x, event.y, app.color, app.r
            app.dots.append((cx, cy, color, r))

# changes the color based on which color box is clicked
def changeColor(app, event, colorNum):
    if clickedInBox(app, event.x, event.y, colorNum):
        app.erasing = False
        app.color = app.colors[colorNum]

# actions when mouse is pressed
def mousePressed(app, event):
    # sets mode to erasing/not erasing based on box clicked
    if clickedInBox(app, event.x, event.y, 0): app.erasing = False
    if clickedInBox(app, event.x, event.y, 1): app.erasing = False
    if clickedInBox(app, event.x, event.y, 2): app.erasing = False
    if clickedInBox(app, event.x, event.y, 3): app.erasing = True
    # erases dot at mouse position
    if app.erasing:
        dot = clickedInDot(app, event.x, event.y)
        if dot: app.dots.remove(dot)
    # changes color based on box clicked
    else:
        for i in range(3):
            changeColor(app,event,i)

# checks if given x and y values are in the specified box
def clickedInBox(app, x, y, boxNum):
    return ((app.width-app.margin-app.sqSize <= x <= app.width-app.margin) and
            (app.margin+boxNum*app.sqSize <= y <= app.margin+(boxNum+1)*app.sqSize))

# checks if given x and y values are in any of the dots in app.dots
def clickedInDot(app, x, y):
    for dot in app.dots:
        cx, cy, _, r = dot
        if cx - r <= x <= cx + r and cy - r <= y <= cy + r:
            return dot
    return False

# checks if given x and y values are on the slider in order to move it
def clickedOnSlider(app, x, y):
    return app.slideX - app.slideR <= x <= app.slideX + app.slideR and \
       app.slideY - 1.5*app.slideR <= y <= app.slideY + 1.5*app.slideR

# checks if x and y values are in the slide box in order to not continue drawing
# if they are
def clickedInSlideBox(app, x, y):
    return .4*app.lineX <= x <= 1.6*app.lineX and app.lineY - .6*app.margin \
            <= y <= app.lineY + .6*app.margin

# gets the coords of the box of the specified color
def getColorCoords(app, colorNum):
    x0 = app.width - app.margin - app.sqSize
    x1 = app.width - app.margin
    y0 = app.margin + colorNum*app.sqSize
    y1 = app.margin + (colorNum+1)*app.sqSize
    return x0,y0,x1,y1

# draws boxes with possible colors
def drawColors(app, canvas):
    for i in range(len(app.colors)):
        x0,y0,x1,y1 = getColorCoords(app,i)
        canvas.create_rectangle(x0,y0,x1,y1,fill=app.colors[i])

# draws the erase button
def drawEraseButton(app, canvas):
    canvas.create_oval(app.width - app.margin - app.sqSize, 
                            app.margin + 3*app.sqSize,
                            app.width - app.margin,
                            app.margin + 4*app.sqSize, fill='white')
    canvas.create_text(app.width-app.margin-.5*app.sqSize,
                       app.margin + 3.5*app.sqSize,
                       text = "Erase",
                       font = "Arial 20 bold")

# draws a single dot with the color attributed to the image
def drawDot(app, canvas, cx, cy, color, r):
    canvas.create_oval(cx-r,cy-r,cx+r,cy+r,
                           fill=color,outline=color)

# draws the slider and slider box at the bottom of the canvas
def drawSlider(app, canvas):
    canvas.create_rectangle(.4*app.lineX, app.lineY - .6*app.margin,
                            1.6*app.lineX, app.lineY + .6*app.margin,
                            fill="white",outline="black")
    canvas.create_rectangle(.5*app.lineX, app.lineY - 1,
                            1.5*app.lineX, app.lineY + 1,
                            fill='black')
    canvas.create_oval(app.slideX-app.slideR,app.slideY-app.slideR,
                       app.slideX+app.slideR,app.slideY+app.slideR,
                       fill='black')

def redrawAll(app, canvas):
    for dot in app.dots:
        cx, cy, color, r = dot
        drawDot(app, canvas, cx, cy, color, r)
    drawColors(app, canvas)
    drawEraseButton(app, canvas)
    drawSlider(app, canvas)

runApp(width=800,height=800)