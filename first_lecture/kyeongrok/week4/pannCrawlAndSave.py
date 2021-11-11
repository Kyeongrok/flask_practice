from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pann.nate.com/talk/c20038")
bsObj = BeautifulSoup(html, "html.parser")
trList = bsObj.find("table", {'class':'talk_list'}).find("tbody").findAll("tr")
# print(trList)

list = ['hello', 'bye']

# print(divLisWrap)

for a in trList:
    print(a)
