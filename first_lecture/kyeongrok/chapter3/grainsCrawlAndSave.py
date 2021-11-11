from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://bepi.mpob.gov.my/index.php/en/statistics/price/daily.html")
bsObj = BeautifulSoup(html, "html.parser")

print(bsObj)

# subTable = bsObj.find('div', {'class':'sub01-table'})
#
# print(subTable)



