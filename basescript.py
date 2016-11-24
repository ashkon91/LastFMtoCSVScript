from urllib2 import urlopen
import json
import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)


url = 'http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user=ashkon91&api_key=361fad39798b9291b9cb37f447c829cc&format=json'
urltracks = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=ashkon91&api_key=361fad39798b9291b9cb37f447c829cc&format=json'

data = urlopen(url)
response = data.read()
vals = json.loads(response)
songs = []
def songsPerPage(urltracks, pagenum):
	print pagenum
	song = []
	info = {'limit':'200','page':pagenum}
	response2 = requests.get(urltracks, data=info )
	json_data = json.loads(response2.text)
	pp.pprint(json_data['recenttracks'])
	for track in json_data['recenttracks']['track']:
		song.append(track['name'])
	return song

doto = {'limit':'200'}
responsedata = requests.get(urltracks, data = doto)
jsond = json.loads(responsedata.text)
totalPages = int(jsond['recenttracks']['@attr']['totalPages'])

for i in range(totalPages):
	songs += songsPerPage(urltracks, str(i+1))
	print len(songs)
print len(songs)
