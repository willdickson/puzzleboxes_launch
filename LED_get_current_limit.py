#!/usr/bin/env python

#Basic imports
from ctypes import *
import sys
#Phidget specific imports
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import AttachEventArgs, DetachEventArgs, ErrorEventArgs
from Phidgets.Devices.LED import LED, LEDCurrentLimit, LEDVoltage
from time import sleep
from Phidgets.Phidget import PhidgetLogLevel    


limit_to_string = {
        LEDCurrentLimit.CURRENT_LIMIT_20mA: '20mA',
        LEDCurrentLimit.CURRENT_LIMIT_40mA: '40mA',
        LEDCurrentLimit.CURRENT_LIMIT_60mA: '60mA',
        LEDCurrentLimit.CURRENT_LIMIT_80mA: '80mA',
        }


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

if __name__== "__main__":

    limit = led.getCurrentLimit()
    print('current limit = {}'.format(limit_to_string[limit]))






    

