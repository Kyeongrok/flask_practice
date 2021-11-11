from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://rss.itunes.apple.com/api/v1/kr/apple-music/hot-tracks/all/10/explicit.json")
print(html)