from urllib.request import urlopen
# html = urlopen("https://rss.itunes.apple.com/api/v1/kr/apple-music/hot-tracks/all/10/explicit.json")
# print (html)

import json
content = urlopen('https://rss.itunes.apple.com/api/v1/kr/apple-music/hot-tracks/all/10/explicit.json')
apiResult =json.load(content)
results = apiResult['feed']['results']

# print(results)

f = open("새파일.txt", 'w', encoding='utf-8')


for result in results:
    # print(result)
    artistNames = result['artistName']
    collectionNames = result['collectionName']
    twoName = artistNames + "/" + collectionNames
    print(twoName)
    f.write(str(twoName) + "\n")

