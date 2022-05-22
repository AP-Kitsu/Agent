import json
import io

def openJson():
        datajson = json.load(io.open('C:\\Users\\Kitsu\\PycharmProjects\\Agent\\data\\psjsonUTF8.json', 'r', encoding='utf-8-sig'))
        print(datajson)

print(openJson())

