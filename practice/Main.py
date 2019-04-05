import json
from contextlib import suppress
from CheckLocation import checkLocation
from collections import Counter
import time

start_time = time.time()
numberCounter = []
tags_dict = {}
checkLocation = checkLocation()


def countTopFive(tagCounter):
    tempo = tagCounter[0][1]
    counter = 1
    list_1 = []
    for k, v in tagCounter:
        if tempo > v:
            tempo = v
            counter = counter + 1
        if counter > 5:
            break
        list_1.append([str(k), str(v)])
    return list_1

def searchTags(text, location):
    start = 1
    end = -2
    word_list = text.split()
    if text[0] == " ":
        start = 0
    if text[-1] == " ":
        end = -1
    for word in word_list[start: end]:
        if word[0] == "#":
            if location not in tags_dict.keys():
                tags_dict[location] = [word.lower()]
            else:
                tags_dict[location].append(word.lower())


with open("ccc/practice/resources/bigTwitter.json") as twitter:
    for line in twitter:
        if line[2: 4] != "id":
            continue
        if line[-2] == ",":
            line = line[:-2]
        info_json = json.loads(line)
        with suppress(Exception):
            x = info_json["doc"]["coordinates"]["coordinates"][0]
            y = info_json["doc"]["coordinates"]["coordinates"][1]
            text = info_json["doc"]["text"]
            if x and y:
                location = checkLocation.getLocation(x, y)
                if location:
                    numberCounter.append(location)
                    searchTags(text, location)

countNumber = Counter(numberCounter)
for key, value in countNumber.most_common():
    print(str(key) + ": " + str(value) + " posts,")
print("Down to the square with the least number of posts;")
print()
# for key in tags_dict:
#     tagCounter = Counter(tags_dict[key]).most_common(5)
#     print(str(key) + ": (", end=""),
#     for key, value in tagCounter:
#         print("(" + str(key) + ", " + str(value) + "),", end=""),
#     print(")")
# print("Down to the top 5 hashtags in the grid cell with the least number of posts;")
for key in tags_dict:
    tagCounter = Counter(tags_dict[key]).most_common()
    list_topFive = countTopFive(tagCounter)
    print(str(key) + ": (", end="")
    for info in list_topFive[0: len(list_topFive) - 1]:
        print("(" + str(info[0]) + "," + str(info[1]) + "),", end="")
    print("(" + str(list_topFive[-1][0]) + ", " + str(list_topFive[-1][1]) + "))")
end_time = time.time()
print(end_time - start_time)