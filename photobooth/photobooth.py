from picamera import PiCamera
from datetime import datetime
from time import sleep
from gpiozero import Button, LED
from twython import Twython
import random
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Setup twitter with the API keys in auth
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Instantiate the camera
camera = PiCamera()

# Instantiate the button
button = Button(14)

# Instantiate each LED
red = LED(4)
yellow = LED(17)
green = LED(22)
blue = LED(21)


# Random messages for twitter
messages = [
    "Hello world",
    "Hi there",
    "My name is Babbage",
    "What's up?",
    "How's it going?",
    "Have you been here before?",
    "Get a hair cut!",
]

# Loop to take and tweet photos
while True:
    try:
        # Wait for the button to be pressed
        button.wait_for_press()
        timestamp = datetime.now().isoformat()
        photo_path = '/home/pi/Desktop/camera/photos/%s.jpg' % timestamp

        # Turn on LEDs and sleep 1 second between each one
        red.on()
        sleep(1)
        red.off()

        yellow.on()
        sleep(1)
        yellow.off()

        green.on()
        sleep(1)
        green.off()

        # Take a picture and save it to photo_path
        camera.capture(photo_path)

        # Tweet the picture with a random message
        with open(photo_path, 'rb') as photo:
            blue.on()
            message = random.choice(messages)
            response = twitter.upload_media(media=photo)
            twitter.update_status(status=message, media_ids=[response['media_id']])
        blue.off()

    except KeyboardInterrupt:
        camera.stop_preview()
        break
