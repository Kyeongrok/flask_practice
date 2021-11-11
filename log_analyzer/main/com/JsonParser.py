import json

'''
1.파일을 읽는다.
2.읽어서 list로 만든다.
3.json을 읽는다.
4.json을 encoding한다. dict로 뽑힌다.
startTimeStamp, endTimeStamp를 뽑아서 list에 담는다.
list를 파일에 쓴다.
'''
class JsonParser:
    fileLocation = ""
    fromFileName = ""
    targetFileName = ""

    def __init__(self, fileLocation):
        self.fileLocation = fileLocation


    def readFiles(self, sFromFileName):
        with open(self.fileLocation + sFromFileName, mode="rt", encoding='utf-8') as file:
            stringList = file.readlines()
            item = stringList[0]
            print(item)
            print(len(stringList))

            for item in stringList:
                try:
                    jsonObject = json.loads(item)
                    print(jsonObject['startTimestamp'] + " " + jsonObject['endTimestamp'])
                    event =jsonObject['apiResults'][0]['league']['season']['eventType'][0]['events'][0]
                    homeTeam = event['teams'][0]
                    awayTeam = event['teams'][1]
                    print(homeTeam['linescores'])
                    print(awayTeam['linescores'])
                except:
                    print("item : " + item)



