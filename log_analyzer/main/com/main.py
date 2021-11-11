from src.main.com import JsonParser
from src.main.com.LogParser import LogParser

eventId = "1703552"
startDate = "2017-06-15"
fileLocation = "C:/Users/kyeongrok.kim/Desktop/"
fromFileName = "parse_2017-06-15.87.log"
targetFileName = "141000-"+eventId+".txt"
pattern = startDate+" 14:[0-2][1-9]:[0-9][0-9].*startTimestamp.*"+eventId+".*"

logParser = LogParser(fileLocation, fromFileName, targetFileName)
logParser.extractPattern(pattern)
logParser.replaePattern(targetFileName, "json.txt"
                     , "----", "{")

jsonParser = JsonParser(fileLocation)
jsonParser.readFiles("json.txt")


