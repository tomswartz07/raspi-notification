#!/bin/python
from datetime import datetime
import transmissionrpc
import psutil
import imaplib
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
	MAIL_SERVER	= 'mail.pennmanor.net'
	EMAIL_USER	= 'user'
	EMAIL_PASS	= 'password'
	DISK_FS		= ['/','/Elements']
	STATIC_MODE	= False

	def status_date(self):
		mem = psutil.virtual_memory()

		try:
			cpu_temp = float([line.strip() for line in open(self.TEMP_SYS)][0])/1000
		except Exception:
			cpu_temp = 0.0
		return datetime.now().strftime(self.DATE_FMT) + "Mem:%2.1f%% T:%3.1f" % (mem.percent, cpu_temp)

	def status_torrents(self):
		try:
			torrents = transmissionrpc.Client(self.TORRENT_HOST, port=self.TORRENT_PORT, user=self.TORRENT_USER, password=self.TORRENT_PASS)
			stats = torrents.session_stats()
			download = stats.downloadSpeed/1000
			upload = stats.uploadSpeed/1000
			return "Active: %d of %d DL:%dKB UL:%dKB" % (stats.activeTorrentCount, stats.torrentCount, download, upload)
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
		return format('System Starting Up - Loading...')

	def status_email(self):
		try:
			mail = imaplib.IMAP4_SSL(self.MAIL_SERVER)
			mail.login(self.EMAIL_USER, self.EMAIL_PASS)
			mail.select()
			unread = mail.search(None,'UnSeen')
			count = len(unread[1][0].split())
			mail.close()
			return "Penn Manor EmailInbox: %d" % (count)
		except (KeyboardInterrupt, SystemExit):
			mail.close()
			return format('Sys Err. Closing Mail')
		except:
			mail.close()
			return format('IMAP Error')

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
			return "Current Temp:%3.0f High:%.0f Low:%.0f" % (temp_current, temp_high, temp_low)
		except Exception:
			return format('Unable to fetch weather data')

if __name__ == '__main__':
	nt = Notifications()
	nt.status_date()
	nt.startup()
	nt.status_email()
	nt.status_torrents()
	nt.status_weather()
	nt.status_disk()
