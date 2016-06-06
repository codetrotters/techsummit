# Photobooth Gif
This simple [python](https://learnxinyminutes.com/docs/python/) project will take a picture each time a LED lights up and then combine the `3` pictures into a gif which is then uploaded to `Twitter`.

## Flow
- The program waits for the `button` to be pressed.
- Once pressed the Red LED will turn on to take a picture.
- Then the Yellow LED will turn on to take a picture.
- Then the Green LED will turn on to take a picture.
- Then the `3` picures are combined into a gif using the `createGif` method.
- Finally it uploads the `gif` to `Twitter`.

## Auth
The `auth.py` file has the `Twitter` credentials needed for authenticating with the `API ` to send tweets using the Raspberry Pi. It will send a random message with the picture taken.

## Loading
Shows a loading effect using the LEDs while the program creates a gif.
You need to send the LEDs when creating the gif like this: `createGif(leds)`
