#!/usr/bin/python
#Rag Sagar <ragsagar@gmail.com>
#Free to copy, modify and redistribute

import sys 
from urllib2 import urlopen, URLError
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class WeatherFinder(ContentHandler):
	"""the handler class"""
	def __init__(self):
		self.weather_list = []
		self.go_on = False
		
	def startElement(self, tag, attrs):
		"handles the opening tags"
		if tag == 'current_conditions':
			self.go_on = True
		if self.go_on : # so that only values inside current_conditions tag is appended
			if tag == 'condition' :
				self.weather_list.append('Condition: '+attrs.get('data',""))
			elif tag == 'humidity' :
				self.weather_list.append(attrs.get('data',""))			
			elif tag == 'temp_c' :
				self.weather_list.append('Temperature:'+attrs.get('data',"")+'C')
			elif tag == 'wind_condition' :
				self.weather_list.append(attrs.get('data',""))
		return
		
	def endElement(self, tag):
		"handles closing tags"
		if tag == 'current_conditions':
			self.go_on = False

if len(sys.argv) is not 2 :
	print "Syntax : ",sys.argv[0]," <city> \n"
	sys.exit(1)
else :
	city = sys.argv[1]
	url = 'http://www.google.com/ig/api?weather='+city
	parser = make_parser()
	obj = WeatherFinder()
	parser.setContentHandler(obj)
	try :
		parser.parse(urlopen(url))
	except URLError:
		print "\n\033[33m Unable to fetch data..\033[0m\n"
		sys.exit(1)
	if obj.weather_list == [] :
		print "\n\033[33m Invalid city name, Try another.. \033[0m\n "	
	else :
		print "\033[33mWeather Conditions of",city,"\033[36m"
		for i in obj.weather_list:
			print i	
		print "\033[0m"
		
		

