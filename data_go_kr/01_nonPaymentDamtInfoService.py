import requests, xmltodict, json
import pandas as pd

key = "QOIyVxx7oVtU%2B03Na7PG6BWsVsElYmp8921ouUzpePsIOHFnNAOXhlYy4lrwBeG31dKKRfdKRmTY2CY034o2qw%3D%3D"
url = "http://apis.data.go.kr/B551182/nonPaymentDamtInfoService/getNonPaymentItemCodeList?pageNo=1&numOfRows=100&ServiceKey={}".format(key)

content = requests.get(url).content
dict = xmltodict.parse(content)
jsonString = json.dumps(dict['response']['body'], ensure_ascii=False)
jsonObj = json.loads(jsonString)

for item in jsonObj['items']['item']:
    print(item)

file = open("./nonPayment.json", "w+")
file.write(json.dumps(jsonObj['items']['item']))







