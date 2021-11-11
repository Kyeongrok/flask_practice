import re

class LogParser:
    fileLocation = ""
    fromFileName = ""
    targetFileName = ""

    def __init__(self, fileLocation, fromFileName, targetFileName):
        self.fileLocation = fileLocation
        self.fromFileName = fromFileName
        self.targetFileName = targetFileName

    def replaePattern(self, fromFileName, toFileName, sPattern, replaceString):
        '''
        대상 파일을 열어서 <입력된 패턴>을 <입력된 string>으로 바꾼다.
        '''
        print("replace start from : "+fromFileName + " to : "+toFileName)
        with open(self.fileLocation + fromFileName, mode="rt", encoding='utf-8') as fromFile:
            stringList = fromFile.readlines()
            with open(self.fileLocation + toFileName, mode="w", encoding='utf-8') as targetFile:
                pattern = re.compile(sPattern)
                for line in stringList:
                    #여기서 replace를 한다.
                    print(pattern.findall(line))
                    targetFile.write(pattern.sub(replaceString, line))

    def extractPattern(self, sPattern):
        print("start extract")
        with open(self.fileLocation + self.fromFileName, mode="rt", encoding='utf-8') as f:
            string = f.read()

        pattern = re.compile(sPattern)
        findAll = pattern.findall(string)

        print(type(findAll))
        print(len(findAll))

        file = open(self.fileLocation + self.targetFileName, mode="w", encoding='utf-8')
        for item in findAll:
                file.write(item + "\n")
        file.close()
        print("success")
