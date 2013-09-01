#!/bin/python
from datetime import datetime
import urllib2, json

class Notifications:
	TEMP_SYS	= '/sys/class/thermal/thermal_zone0/temp'
	DATE_FMT	= '%a %b %d %H.%M'
	TORRENT_HOST	= 'remote.tswartz.net'
	TORRENT_PORT	= '1776'
	TORRENT_USER 	= 'user'
	TORRENT_PASS	= 'pass'
	WEATHER_CITY	= 'Lancaster'
	DISK_FS		= ['/','/Elements']
	STATIC_MODE	= False

	def status_date(self):
		return [datetime.now().strftime(self.DATE_FMT)]

	def startup(self):
		return ['{:^16}'.format('System'),
			'{:^16}'.format('Starting up')]

if __name__ == '__main__':
	nt = Notifications()
	print '-------------'
	print 'Notifications:'
	print '-------------'
	print '\n'.join(nt.status_date())
	print '-------------'
	print '\n'.join(nt.startup())
	print '-------------'
