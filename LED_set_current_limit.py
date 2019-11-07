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
string_to_limit = {v:k for k,v in limit_to_string.items()}


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



limit_str = sys.argv[1]
limit_val = string_to_limit[limit_str]
print('set current limit to {} ({})'.format(limit_str, limit_val))
led.setCurrentLimit(limit_val)

sleep(0.5)

limit = led.getCurrentLimit()
print('get current limit = {}'.format(limit_to_string[limit]))

#Create an LED object
try:
    led = LED()
except RuntimeError as e:
    print("Runtime Exception: %s" % e.details)
    print("Exiting....")
    exit(1)








    

