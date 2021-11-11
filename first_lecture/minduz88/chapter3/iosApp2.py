from urllib.request import urlopen
import json

html = urlopen("https://rss.itunes.apple.com/api/v1/kr/macos-apps/top-free-mac-apps/all/10/explicit.json")
print(html)
