#!/usr/bin/python
# lightLEDs.py
# Button press loops through LEDs like this (0 is led off, 1 is led on): 000, 100, 110, 111, 011, 001, 000, 100, 110, 111, 011, 001, 000 etc.
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

def setLEDs(tempArray):
  GPIO.output(11, tempArray[0])
  GPIO.output(13, tempArray[1])
  GPIO.output(21, tempArray[2])
  
array=[[0,0,0],[1,0,0],[1,1,0],[1,1,1],[0,1,1],[0,0,1]]

a=0

try:
  while True:
    while GPIO.input(26)==1:
      time.sleep(0.1)
    setLEDs(array[a%6])
    a=a+1
    while GPIO.input(26)==0:
      time.sleep(0.1)
finally:
  GPIO.cleanup()
  sys.exit(0)
