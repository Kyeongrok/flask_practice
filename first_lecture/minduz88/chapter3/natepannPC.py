# 네이트판 pc버전 30대 제목 추출
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://m.pann.nate.com/talk/c20003")
bsObj = BeautifulSoup(html, "html.parser")

urList = bsObj.find("")