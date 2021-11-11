fileName = "C:/Users/kyeongrok.kim/Desktop/parse_2017-05-31.1.log"

def getFileContents(file_path):
    f1= open(file_path, 'rt', encoding='utf-8')
    f1.readline();
    return f1.read()

#print(getFileContents(fileName))

#[gidx= 로 시작하는 라인을 추출해서 다른 파일로 빼낸다.
#특정 gidx를 포함하고 있는 라인을 추출한다.
fileName = "C:/Users/kyeongrok.kim/Desktop/parse_2017-05-31.1.log"
def printLineByLine(file_path, regexp):
    with open(file_path, 'rt', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
#printLineByLine(fileName)
