# Photobooth
This simple [python](https://learnxinyminutes.com/docs/python/) project will take a picture and upload it to Twitter on the Codetrotter's account.

## Flow
- The program waits for the `button` to be pressed.
- Once pressed the LEDs will flash `red`, `yellow` and finally `green`.
- It takes a `picture`
- It uploads the `picture` to `Twitter`

## Auth
The auth.py file has the `Twitter` credentials needed for authenticating with the API to send tweets with the Raspberry Pi. It will send a random message with the picture taken.
