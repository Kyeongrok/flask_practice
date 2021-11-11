from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pann.nate.com/")
bs0bj = BeautifulSoup(html, "html.parser")

print(bs0bj)

nameList = bs0bj.findAll("a")
print(nameList)
