from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import re


url = 'http://www.r114.com/z/real/m_dong.asp?pg=1&startpage=2&only=0&m_=5&g_=&type_g=A&type_cd=03%5E05%5E&addr1=%BC%AD%BF%EF%C6%AF%BA%B0%BD%C3&addr2=%B0%AD%B3%B2%B1%B8&addr3=%BF%AA%BB%EF%B5%BF&mpl=15000&mph=16000&SF_PKVal=6&SF_Size=0&rNumber=5791&type_m=m&type=m&searchok='
url = 'http://www.r114.com/z/real/m_dong.asp?only=0&m_=5&g_=&type_g=A&type_cd=03%5E05%5E&addr1=%BC%AD%BF%EF%C6%AF%BA%B0%BD%C3&addr2=%B0%AD%B3%B2%B1%B8&addr3=%BF%AA%BB%EF%B5%BF&mpl=15000&mph=16000&SF_PKVal=6&SF_Size=0&rNumber=5791&lst=ml&order=%B8%C5%B8%C5%B0%A1&sort=desc&type=m&type_m=m'

html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")

trList = bsObj.find('table', {'class':'rowTb_new row_line_new'})\
    .find('tbody').findAll('tr')

print(len(trList))

for tr in trList:
    try:
        price = tr.find('td', {'class':'ar new_price'}).text
        price = re.sub('\s+', '', price)
        href = tr.find('a', {'class':'blue in_view_link'})['href']
        name = tr.find('a', {'class':'blue in_view_link'}).text
        size = tr.find('td', {'class':'ac'}).find('a').find('span').text
        size = re.sub('\s+', '', size)
        print('{},{},{},http://www.r114.com/z/real/{})'.format(name, price.replace(',', ''), size, href))
    except:
        1 + 1



