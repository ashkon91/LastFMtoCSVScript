from urllib2 import urlopen
import json
import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

url = 'http://ws.audioscrobbler.com/2.0/'

data = urlopen(url)
response = data.read()
vals = json.loads(response)
songs = []
def songsPerPage(url, pagenum):
    song = []
    payload = {'method':'user.getrecenttracks', 'user':user, 'api_key':api_key, 'limit':'200', 'page':pagenum, 'format':'json'}
    response = requests.get(url, data=payload )
    json_data = json.loads(response.text)

    for track in json_data['recenttracks']['track']:
        song.append(track['name'])
    return song

testpayload = { 'method':'user.getrecenttracks', 'user':'ashkon91', 'api_key': '361fad39798b9291b9cb37f447c829cc', 'format':'json'}

responsedata = requests.get(url, params = testpayload)
jsond = json.loads(responsedata.text)
totalPages = int(jsond['recenttracks']['@attr']['totalPages'])
print totalPages

for i in range(totalPages):
    songs += songsPerPage(urltracks, str(i+1))
