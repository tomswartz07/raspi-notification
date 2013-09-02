raspi-notification
==================

Raspberry Pi LCD Notifier is a Python program used to display text on a Parallax model 27977 2x16 LCD Module.

This program uses basic-level commands sent to the serial interface of the LCD Module. Some other freely available libraries use a fuller interface to communicate with the serial interface.

## Requirements
### Software Requirements
* Python2 - There were some changes to the way that strings are handled in Python3
* Python-Transmissionrpc
* Python-pyserial

### Hardware Requirements
* Raspberry Pi Model B - Most modules will not work with the Model A
* Parallax Model 27977 2x16 Serial LCD Module
* 3 wires to connect to the GPIO Pins and LCD Module

## Instructions

You could simply run the script daemon.py manually, or add it to an autostart module (rc script, perhaps?)

You may need superuser rights to access /dev/ttyAMA0.

As the script runs, it will write all of the text from the statusline modules to the screen.

### Future Plans
I hope to build this python group out and create a full class for the Parallax screen.
This would allow the daemon script to be modified and used on any common LCD or commandline tool, as opposed to the current 'hard-code' method.
