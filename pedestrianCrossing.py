#!/usr/bin/python
# pedestrianCrossing.py
# goes red, yellow, green, waits for button press, yellow, red, yellow, green etc like a pedestrain crossing
# Author : Zachary Igielman

import RPi.GPIO as GPIO, time, sys

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT) #red
GPIO.setup(13, GPIO.OUT) #amber
GPIO.setup(21, GPIO.OUT) #green
GPIO.setup(26, GPIO.IN) #button

GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(21, GPIO.LOW)

def setLEDs(red,amber,green):
  GPIO.output(11, red)
  GPIO.output(13, amber)
  GPIO.output(21, green)

try:
  while True:
    setLEDs(1,0,0)
    time.sleep(5)
    setLEDs(1,1,0)
    time.sleep(2)
    setLEDs(0,0,1)
    while GPIO.input(26)==0:
      time.sleep(0.1)
    setLEDs(0,1,0)
    time.sleep(2)
finally:
  GPIO.cleanup()
  sys.exit(0)
