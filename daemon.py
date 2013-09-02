#!/bin/python
from time import sleep
from notifications import Notifications
import serial

# Serial connection to LCD Module
lcd = serial.Serial(port='/dev/ttyAMA0',baudrate=9600)

# Format is 'message'; time to display,
NOTIFY_SETTINGS = {
	'startup':	5,
	'status_date':	3,
	'status_weather': 2,
	'status_disk':	2,
	}

# Initialize the notifications class
nt = Notifications()

# Loop through the list of settings and display
while True:
	for i, (TIMEOUT) in NOTIFY_SETTINGS.iteritems():
		msg = getattr(nt, i)()
		if len(msg):
			lcd.write(msg)
#			print(i)
			print(msg)
			print(TIMEOUT)
			sleep(TIMEOUT)
#			sleep(3)
