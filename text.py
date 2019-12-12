from twilio.rest import Client

import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim

import os, random, requests, json


class Messenger:

	def __init__(self, from_, to):
		account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
		auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
		self.client = Client(account_sid, auth_token)
		self.to = to
		self.from_ = from_
		

	def sendMessage(self, body):
		message = self.client.messages.create(
                     body=body,
                     from_=self.from_,
                     to=self.to
                 )

		return message.sid

	def getQuote(self):
		with open('quotes.json', 'r+') as file:
			quotes = json.load(file)
		quoteData = random.choice(quotes)
		quote = "\"" + quoteData['content'] + "\"" + " - " + quoteData['author']
		# body = "Daily Quote\n" + quote + "\n"
		body = quote + "\n"
		return body

	def getWeather(self, location):
		# get coordinates based off location
		ctx = ssl.create_default_context(cafile=certifi.where())
		geopy.geocoders.options.default_ssl_context = ctx
		geolocator = Nominatim(scheme='http')
		locationData = geolocator.geocode(location)
		longitude = str(locationData.longitude)
		latitude = str(locationData.latitude)


		# get weather from darksky API using coordinates
		r = requests.get("https://api.darksky.net/forecast/2451885ebe3019d24ec17a60f151422b/"+latitude+","+longitude+"")
		data = r.json()
		todayData = data['daily']['data'][0]


		todayLow = round(todayData['temperatureLow'])
		todayHigh = round(todayData['temperatureHigh'])
		currentSummary = data['currently']['summary']
		current = round(data['currently']['temperature'])


		# form text body and send message
		body = "It is {}ºF and {}\nLow {}ºF | High {}ºF\n".format(current, currentSummary, todayLow, todayHigh) 
		return body














