import pyglet
import math

# Initialize the window
# I wouldn't reccomend resizing the window as I fear the visuals may break, try at your own risk 
window = pyglet.window.Window(1024, 640)
window.set_caption('Sonar')

# Draws the background of the sonar, the objects drawn will not move
def drawBg():
    for x in range(0, 216, 36): # Draw 6 lines, aesthetic purposes only 
        addGreenLine(x, 60).draw()
    pyglet.shapes.Circle(x=window.width/2, y=50, radius=496, color=(50, 225, 30, 50)).draw() # Background for the sonar
    for x in range(496, 0, -124): # Draw 4 circles on the screen
        pyglet.shapes.Arc(x=window.width/2, y=50, radius=x, color=(50, 225, 30), thickness=5).draw()
    pyglet.shapes.Rectangle(x=0, y=0, width=window.width, height=50, color=(0, 0, 0)).draw() # Cover up the bottom of the screen with a black rectangle to add space for text

# Draws text onto the sonar, this will update with new information
def drawText(dist, angle):
    distLabel = pyglet.text.Label(text="Distance: " + dist + "cm", x=10, y=-5, font_name='Lucida Sans Unicode', font_size=28, anchor_x='left',anchor_y='bottom', color=(50, 225, 30))
    distLabel.draw()
    angLabel = pyglet.text.Label(text="Angle: " + angle + "degrees", x=610, y=-5, font_name='Lucida Sans Unicode', font_size=28, anchor_x='left',anchor_y='bottom', color=(50, 225, 30))
    angLabel.draw()

# Draws the scanning angle, this just turns
def drawScanningLine(angle):
    # Using some basic trigonometry to get the positions of x2 and y2 by finding the
    # height of a triangle with hypotenuese = 496 and the angle provided
    x2 = 496 * math.cos(math.radians(angle)) + window.width/2
    x2 = map_value(x2)
    y2 = 496 * math.sin(math.radians(angle)) + 50
    line = pyglet.shapes.Line(x=window.width/2, y=50, x2=x2, y2=y2, width=7, color=(0, 255, 140))
    line.draw()

def addRedLine(angle, dist):
    # Using some basic trigonometry, find x,y2,y2 given the hypotenuse that is the radius of the circle times the (distance/max distance) and the angle given 
    dist = 496 * (dist/60)
    x = dist * math.cos(math.radians(angle)) + window.width/2
    x = map_value(x)
    y = dist * math.sin(math.radians(angle)) + 50
    x2 = 496 * math.cos(math.radians(angle)) + window.width/2
    x2 = map_value(x2)
    y2 = 496 * math.sin(math.radians(angle)) + 50
    line = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=7, color=(255, 0, 0))
    return line

def addGreenLine(angle, dist):
    # Similar to the function above, do some basic trigonometry to find the x,y,x2,y2 of the green line
    dist = 496 * (dist/60)
    x = window.width/2
    y = 50
    x2 = dist * math.cos(math.radians(angle)) + window.width/2
    x2 = map_value(x2)
    y2 = dist * math.sin(math.radians(angle)) + 50
    line = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=7, color=(0, 255, 0))
    return line

# I used this to fix a reversing error, not entirely sure why that error is occuring
def map_value(value):
    # Reverse the value
    return abs(value - window.width)
