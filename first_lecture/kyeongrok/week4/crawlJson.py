from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

content = urlopen('https://api.github.com/')

apiJson = json.load(content)
print (apiJson['current_user_url'])

file = open("새파일.txt", 'w', encoding='utf-8')
file.write( str(apiJson) + "\n")
