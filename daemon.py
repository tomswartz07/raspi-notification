#!/bin/python
from time import sleep
from notifications import Notifications
import serial

# Serial connection to LCD Module
lcd = serial.Serial(port='/dev/ttyAMA0',baudrate=9600)

# Format is 'message'; time to display,
NOTIFY_SETTINGS = {
	'startup':	9,
	'status_date':	9,
	'status_weather': 2,
	'status_disk':	2,
	}

# Initialize the notifications class
#nt = Notifications()

# Set up the screen for first run
lcd.write('x\0C') # Carriage Return (Clear any text)
sleep(1) # Necessary delay after clearing display
lcd.write('x\16') # Display on, no cursor, no blink
lcd.write('x\11') # Backlight on

# Loop through the list of settings and display
while True:
	for i, (TIMEOUT) in NOTIFY_SETTINGS.iteritems():
		msg = getattr(nt, i)()
		if len(msg):
			lcd.write(msg)
			print(msg)
			print(TIMEOUT)
			sleep(TIMEOUT)
