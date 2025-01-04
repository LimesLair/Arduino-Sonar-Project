import pyglet
import serial
from frontEndLib import *

# Serial port initializtion: COM3, baud rate of 9600 
ser = serial.Serial()   
ser.port = 'COM3' # If facing connectivity errors, just change the port
ser.baudrate = 9600
ser.open()
global redLines, greenLines
redlines = []
greenLines = []
# Defining the main loop of the application
@window.event
def on_draw():
    # Rather than giving a nasty error, just handle the situation where the microcontroller is disconnected
    try:
        # Retrieve information from the microcontroller
        inputLine = ser.readline()
        inputLine = inputLine.decode('utf-8')
        # Store into variables
        inputLine = inputLine.split(' ')
        distance = inputLine[0]
        direction = inputLine[1]
    except:
        print("Sonar device no longer detected, closing application")
        window.close()
        pyglet.app.exit()
        return

    # Clear the window
    window.clear()

    # Draw the background of the sonar
    drawBg()

    # Draw the text
    drawText(distance, direction)

    # Draw the scanning line
    drawScanningLine(int(direction))

    # Add the green lines to its list, the green lines are for aesthetic purposes
    greenLines.append(addGreenLine(int(direction), int(distance)))

    # If something is detected within the range, create a red line and store it
    if (int(distance)<60):
        redlines.append(addRedLine(int(direction), int(distance)))
    
    # This code draws the red lines and creates their fading effect
    for line in redlines:
        line.draw()
        line.opacity -= 3
        if (line.opacity <=0): # Remove once invisible
            redlines.remove(line)
    
    # Draw the green lines and create their fading effect
    for line in greenLines:
        line.draw()
        line.opacity -= 3
        if (line.opacity <=0): # Remove once invisible
            greenLines.remove(line)


# Start the application, aka run the main loop
try:
    pyglet.app.run()
except AttributeError: # Only thrown when removing the device before closing the app
    pass
except: # In case of other errors
    print("An error occured, please try again, or attempt to debug if issue persists")
