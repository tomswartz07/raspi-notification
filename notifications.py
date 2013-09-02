#!/bin/python
from datetime import datetime
import urllib2, json
import subprocess

class Notifications:
	TEMP_SYS	= '/sys/class/thermal/thermal_zone0/temp'
	DATE_FMT	= '%a %b %d %H.%M'
	TORRENT_HOST	= 'remote.tswartz.net'
	TORRENT_PORT	= '1776'
	TORRENT_USER 	= 'user'
	TORRENT_PASS	= 'pass'
	WEATHER_CITY	= '5197079'
	DISK_FS		= ['/','/Elements']
	STATIC_MODE	= False

	def status_date(self):
		return datetime.now().strftime(self.DATE_FMT)

	def status_disk(self):
		try:
			info = []
			for disk in self.DISK_FS:
				df = subprocess.Popen(['df', disk],
					stderr=subprocess.PIPE, stdout=subprocess.PIPE)
				output = df.communicate()[0]
				device, size, used, available, percent, mountpoint = \
					output.split('\n')[1].split()
				resp.append('%-12s %3s' % (disk[:12], percent))
			return info
		except Exception:
			return format('Unable to Load Disk Usage')

	def startup(self):
		return format('System Starting Up')

	def _fetchJson(self, url):
		try:
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
		except Exception:
			return {}
		return response.read()

	def status_weather(self):
		url = 'http://api.openweathermap.org/data/2.5/weather?id=' + self.WEATHER_CITY
		try:
			data.json.loads(self._fetchJson(url))
			status = data['weather'][0]['main'].encode('utf-8')
			temp_current = data['main']['temp']
			temp_high = data['main']['temp_max']
			temp_low = data['main']['temp_min']
			return temp_current, temp_high, temp_low
		except Exception:
			return format('Unable to fetch weather')

if __name__ == '__main__':
	note = Notifications()
	note.status_date()
	note.startup()
	note.status_weather()
	note.status_disk()
