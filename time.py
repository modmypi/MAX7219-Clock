#!/usr/bin/env python

import max7219.led as led
import time
from datetime import datetime

def clock(device, deviceId):
	try:
		while True:

			now = datetime.now()

			hour = now.hour
			minute = now.minute
			second = now.second
			microsecond = now.microsecond
			millisecond = microsecond / 10000

			dot = second % 2 == 0					# calculate blinking dot
			# Set hours
			device.letter(deviceId, 8, int(hour / 10))		# Tens
			device.letter(deviceId, 7, hour % 10, 1)		# Ones
			# Set minutes
			device.letter(deviceId, 6, int(minute / 10))		# Tens
			device.letter(deviceId, 5, minute % 10, dot)		# Ones
			# Set seconds
			device.letter(deviceId, 4, int(second / 10))		# Tens
			device.letter(deviceId, 3, second % 10)			# Ones
			# Set milliseconds
			device.letter(deviceId, 2, int(millisecond / 10))	# Tenths
			device.letter(deviceId, 1, millisecond % 10)		# Hundredths
			time.sleep(0.01)
	finally:
		device.clear()

device = led.sevensegment()
clock(device, 0)
