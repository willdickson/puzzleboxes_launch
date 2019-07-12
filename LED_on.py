#!/usr/bin/env python

#Basic imports
from ctypes import *
import sys
import time
#Phidget specific imports
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import AttachEventArgs, DetachEventArgs, ErrorEventArgs
from Phidgets.Devices.LED import LED, LEDCurrentLimit, LEDVoltage
from time import sleep
from Phidgets.Phidget import PhidgetLogLevel    


#Create an LED object
try:
    led = LED()
except RuntimeError as e:
    print("Runtime Exception: %s" % e.details)
    print("Exiting....")
    exit(1)


print("Opening phidget object...")

try:
    led.openPhidget()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    exit(1)

print("Waiting for attach....")
try:
    led.waitForAttach(1000)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    try:
        led.closePhidget()
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        exit(1)
    exit(1)

print("Turning ON LED's...")

for i in range(64):
    led.setBrightness(i,100)
    time.sleep(0.001)

