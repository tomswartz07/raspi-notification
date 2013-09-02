#!/bin/python
from datetime import datetime
import transmissionrpc
import urllib2, json
import subprocess

class Notifications:
	TEMP_SYS	= '/sys/class/thermal/thermal_zone0/temp'
	DATE_FMT	= '%a %b %d %H.%M'
	TORRENT_HOST	= 'remote.tswartz.net'
	TORRENT_PORT	= 1776
	TORRENT_USER 	= 'user'
	TORRENT_PASS	= 'password'
	WEATHER_CITY	= '5197079' # CityID from openweathermap.org
	WEATHER_UNIT	= 'imperial'
	DISK_FS		= ['/','/Elements']
	STATIC_MODE	= False

	def status_date(self):
		return datetime.now().strftime(self.DATE_FMT)

	def status_torrents(self):
		try:
			torrents = transmissionrpc.Client(self.TORRENT_HOST, port=self.TORRENT_PORT, user=self.TORRENT_USER, password=self.TORRENT_PASS)
			print(self.TORRENT_HOST, self.TORRENT_PORT, self.TORRENT_USER, self.TORRENT_PASS)
			stats = torrents.session_stats()
			download = stats.downloadSpeed/1000
			upload = stats.uploadSpeed/1000

			return 'Active: %2d (%3d)' % (stats.activeTorrentCount, stats.torrentCount), '%5dKB %4dKB' % (down, up)
		except:
			return format("Unable to parse torrent info")

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
			return format('Unable to Load  Disk Usage')

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
		url = 'http://api.openweathermap.org/data/2.5/weather?id=' + self.WEATHER_CITY + '&units=' + self.WEATHER_UNIT
		try:
			data=json.loads(self._fetchJson(url))
			status = data['weather'][0]['main'].encode('utf-8')
			temp_current = data['main']['temp']
			temp_high = data['main']['temp_max']
			temp_low = data['main']['temp_min']
			return temp_current, temp_high, temp_low
		except Exception:
			return format('Unable to fetch weather data')

if __name__ == '__main__':
	nt = Notifications()
	nt.status_date()
	nt.startup()
	nt.status_torrents()
	nt.status_weather()
	nt.status_disk()
