from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

content = urlopen('https://rss.itunes.apple.com/api/v1/kr/apple-music/hot-tracks/all/10/explicit.json')
apiJson = json.load(content)

file = open("새파일.txt", 'w', encoding='utf-8')

for item in apiJson['feed']['results']:
    print(item)
    info = ""
    info += item['artistUrl']
    info += ',' + item['artistName']
    file.write( str(info) + "\n")