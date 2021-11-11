from urllib.request import urlopen

import json
content = urlopen('http://grains.krei.re.kr/chart/main_chart/index/kind/S/sdate/1972-01-01/edate/2017-11-19')
apiResult = json.load(content)

# print(apiResult)


for result in apiResult:
    # print(result)

    date = result['date']
    settlement = result['settlement']
    volume = result['volume']

    threeName = date + "/" + settlement + "/" + volume

    print(threeName)





