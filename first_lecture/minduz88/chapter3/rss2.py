from urllib.request import urlopen
import json

html = urlopen("https://rss.itunes.apple.com/api/v1/kr/apple-music/hot-tracks/all/10/explicit.json")

apiResult = json.load(html)
results = apiResult['feed']['results']

f = open("songs.txt", 'w', encoding='utf-8')

for result in results:
    f.write(result['artistName']+":"+result['collectionName'] + "\n")