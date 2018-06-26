import googlemaps
import json
import datetime
import threading

def calcDepartureDelta():

	threading.Timer(5.0, calcDepartureDelta).start()
	gmaps = googlemaps.Client(key='AIzaSyCOSHcAsVndDZxtVqx7afJPK1rLCKTBTQc')

	# Request directions via public transit
	now = datetime.datetime.now()
	directions = gmaps.directions("465 English St, London Ontario, Canada",
                                     "Support Services Building, London Ontario, Canada",
                                     mode="transit",
                                     departure_time=now)

	departureDelta = datetime.datetime.fromtimestamp(directions[0]['legs'][0]['departure_time']['value']) - datetime.datetime.now()

	print "Departure Delta:" , departureDelta

	flashes = 0

	if departureDelta > datetime.timedelta(minutes=10):
		flashes = 0

	elif departureDelta <datetime.timedelta(minutes=0):
		flashes = 0
	
	else:
		flashes = int(10 - departureDelta.total_seconds()/60)


	print flashes

calcDepartureDelta()
