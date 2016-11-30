from urllib2 import urlopen
import json
import requests
import pprint
import csv
import sys

f = open(sys.argv[1], 'wt')

pp = pprint.PrettyPrinter(indent=4)

url = 'http://ws.audioscrobbler.com/2.0/'
api_key = '361fad39798b9291b9cb37f447c829cc'

def songsPerPage(url, pagenum, user, api_key):
    songs = []
    payload = {'method':'user.getrecenttracks', 'user':user, 'api_key':api_key, 'limit':'200', 'page':pagenum, 'format':'json'}
    response = requests.get(url, data=payload )
    json_data = json.loads(response.text)
    for track in json_data['recenttracks']['track']:
        song = []
        song.append(track['artist']['#text'])
        song.append(track['name'])
        song.append(stringCleaner(track['date']['#text']))
        songs.append(song)
    return songs

def writeToCSV(songs,f):
    try:
        writer = csv.writer(f)
        writer.writerow( ("ARTIST", "SONG", "DATE") )
        for song in songs:
            writer.writerow( (song[0].encode("utf-8"), song[1].encode("utf-8"), song[2].encode("utf-8") ))    
    finally:
        f.close()

def stringCleaner(song):
    songList = song.split()
    return songList[1] + " "+ songList[2]
    
songs = []

payload = { 'method':'user.getrecenttracks', 'limit':'200','user':'Ashkon91', 'api_key': '361fad39798b9291b9cb37f447c829cc', 'format':'json'}


responsedata = requests.get(url, params = payload)
jsond = json.loads(responsedata.text)
totalPages = int(jsond['recenttracks']['@attr']['totalPages'])
print totalPages
for i in range(totalPages):
    print i,len(songs)
    songs += songsPerPage(url, str(i+1), 'Ashkon91', api_key )

writeToCSV(songs,f)

