#!/bin/python
from time import sleep
from notifications import Notifications
import serial

lcd = serial.Serial(port='/dev/ttyAMA0',baudrate=9600)

NOTIFY_SETTINGS = {
	'status_date':	[30],
	}
while True:
	for i, (TIMEOUT) in NOTIFY_SETTINGS.iteritems():
		lcd.write(i)
		sleep(TIMEOUT)
		lcd.write("Moving to next")
