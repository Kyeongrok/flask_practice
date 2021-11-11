from urllib.request import urlopen
import json

html = urlopen("https://rss.itunes.apple.com/api/v1/kr/ios-apps/new-apps-we-love/all/10/explicit.json")

print(str(html))
