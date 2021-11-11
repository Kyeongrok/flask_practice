from urllib.request import urlopen
import json

html = urlopen("https://rss.itunes.apple.com/api/v1/kr/apple-music/hot-tracks/all/10/explicit.json")

apiResult = json.load(html)
results = apiResult['feed']['results']

file = open("새파일.txt", 'w', encoding='utf-8')
for result in results:
    artistNameName = result['artistName'] + ":" + result['name']
    print(artistNameName)
    file.write(artistNameName + "\n")
