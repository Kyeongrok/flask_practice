from urllib.request import urlopen
import json

html = urlopen("http://grains.krei.re.kr/chart/main_chart/index/kind/S/sdate/2017-01-01/edate/2017-11-19")

apiResult = json.load(html)

file = open("새파일.txt", 'w', encoding='utf-8')
for item in apiResult:
    print(item)
