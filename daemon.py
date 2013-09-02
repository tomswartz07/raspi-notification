#!/bin/python
from time import sleep
from notifications import Notifications
import serial

# Serial connection to LCD Module
lcd = serial.Serial(port='/dev/ttyAMA0',baudrate=9600)

# Format is 'message'; time to display,
NOTIFY_SETTINGS = {
	'status_date':	9,
	'status_torrents': 9,
	'status_weather': 9,
	'status_disk':	9,
	}

# Initialize the notifications class
nt = Notifications()

# Set up the screen for first run
lcd.write(chr(12)) # Carriage Return (Clear any text)
sleep(1) # Necessary delay after clearing display
lcd.write(nt.startup())
lcd.write(chr(22)) # Display on, no cursor, no blink
lcd.write(chr(17)) # Backlight on
sleep(3)

# Loop through the list of settings and display
while True:
	for i, (TIMEOUT) in NOTIFY_SETTINGS.iteritems():
		msg = getattr(nt, i)()
		if len(msg):
			lcd.write(chr(12))
			sleep(1)
			lcd.write(msg)
			print(msg)
			sleep(TIMEOUT)
