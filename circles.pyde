# random starting RGB values
r, g, b =  round(random(0,255)), round(random(0,255)), round(random(0,255))

# window width and height
w, h = 600, 400

# radius of circle, pigment value modifier, distance between circles
# default values = 50, 20, 20
RADI = 10
COLOUR_STEP = 30
DISTANCE = 25

def randomise():
    global r, g, b
    rand = ceil(random(0,3))
    if rand == 1:
        r = abs(r - (round(random(-1, 1)) * COLOUR_STEP))
        if r > 250: 
            r = 240
    elif rand == 2:
        g = abs(g - (round(random(-1, 1)) * COLOUR_STEP))
        if g > 250: 
            g = 240
    else:
        b = abs(b - (round(random(-1, 1)) * COLOUR_STEP))
        if b > 250: 
            b = 240
    #print(r, g, b)

def setup():
    size(w, h)
    background(255)
    
    x, y = 0, 0
    
    for dy in range(0, h / DISTANCE + 1):
        for dx in range(0, w / DISTANCE + 1):
            draw_circle(x + (dx * DISTANCE), y + (dy * DISTANCE))
         
    #save('Examples/out1.png')

def draw_circle(x, y):
    randomise()
    fill(r, g, b)
    noStroke()
    blendMode(DARKEST)
    circle(x, y, RADI)
