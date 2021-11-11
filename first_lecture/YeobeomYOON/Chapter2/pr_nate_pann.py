from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html, "html.parser")

print(bs0bj)

nameList = bs0bj.findAll(text="the prince")
print(nameList)
print(len(nameList))

print(len([1, 2]))