import json
from CheckLocation import checkLocation
from printTagNumber import printTagNumber
import time
from printTwitterNumber import printTwitterNumber

numberCounter = []
tags_dict = {}
checkLocation = checkLocation()

start_time = time.time()

def searchTags(text, location):
    start = 1
    end = -1
    word_list = text.split()
    if text[0] == " ":
        start = 0
    if text[-1] == " ":
        end = len(word_list)
    for word in word_list[start: end]:
        if word[0] == "#":
            if location not in tags_dict.keys():
                tags_dict[location] = [word.lower()]
            else:
                tags_dict[location].append(word.lower())


with open("resources/tinyTwitter(3).json") as twitter:
    for line in twitter:
        if line[2: 4] != "id":
            continue
        if line[-2] == ",":
            line = line[:-2]
        info_json = json.loads(line)
        if info_json["doc"]["coordinates"]:
            x = info_json["doc"]["coordinates"]["coordinates"][0]
            y = info_json["doc"]["coordinates"]["coordinates"][1]
        elif info_json["doc"]["geo"]:
            x = info_json["doc"]["geo"]["coordinates"][1]
            y = info_json["doc"]["geo"]["coordinates"][0]
        else:
            continue
        text = info_json["doc"]["text"]
        if x and y:
            location = checkLocation.getLocation(x, y)
            if location:
                numberCounter.append(location)
                searchTags(text, location)

TwitterNumber = printTwitterNumber(numberCounter)
TwitterNumber.printIt()
TagNumber = printTagNumber(tags_dict)
TagNumber.printIt()

end_time = time.time()
print(end_time - start_time)