from time import sleep
import threading
from subprocess import call

# Flash leds to show a loading effect
def loading(e, t, leds):
    while not e.isSet():
        event_is_set = e.wait(t)
        if event_is_set:
            for led in range(0,3):
                leds[led].off()
        else:
            for led in range(0,3):
                leds[led].on()
                sleep(.20)
                leds[led].off()

def createGif(leds):
    # For loading
    event = threading.Event()
    thread = threading.Thread(name='non-block', target=loading, args=(event, 0, leds))
    # Start loading
    thread.start()
    # Use imagemagick to convert images to gif
    call(['convert',
          '/home/pi/Desktop/camera/animation/*.jpg',
          '/home/pi/Desktop/camera/animation/animation.gif'])

    # Delete all the single images
    call(['rm /home/pi/Desktop/camera/animation/*.jpg'], shell=True)
    # Stop loading
    event.set()
