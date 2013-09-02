raspi-notification
==================

Raspberry Pi LCD Notifier is a Python program used to display text on a Parallax model 27977 2x14 LCD Module.

This program uses basic-level commands sent to the serial interface of the LCD Module. Some other freely available libraries use a fuller interface to communicate with the serial interface.

## Requirements
# Software Requirements
* Python2 - There were some changes to the way that strings are handled in Python3
* Python-Transmissionrpc
* Python-pyserial

# Hardware Requirements
* Raspberry Pi Model B - Most modules will not work with the Model A
* Parallax Model 27977 2x14 Serial LCD Module
* 3 wires to connect to the GPIO Pins and LCD Module
