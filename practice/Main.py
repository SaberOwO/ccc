import json
from CheckLocation import checkLocation
from collections import Counter
import time
start_time = time.time()
# readTwitter = readTwitter()
# readTwitter.readingInfo()
# countNumber = Counter(readTwitter.numberCounter)
# for key, value in countNumber.most_common():
#     print(str(key) + ": " + str(value) + " posts,")
# print("Down to the square with the least number of posts;")
# print()
# for key in readTwitter.tags_dict:
#     tagCounter = Counter(readTwitter.tags_dict[key]).most_common(5)
#     print(str(key) + ": (", end=""),
#     for key, value in tagCounter:
#         print("(#" + str(key) + ", " + str(value) + "),", end=""),
#     print(")")
# print("Down to the top 5 hashtags in the grid cell with the least number of posts;")
numberCounter = []
tags_dict = {}
checkLocation = checkLocation()
with open("resources/tinyTwitter(3).json") as twitter:
    for line in twitter:
        if line[2: 4] != "id":
            continue
        if line[-2] == ",":
            line = line[:-2]
        info_json = json.loads(line)
        if info_json["doc"]["coordinates"]["coordinates"][0] and info_json["doc"]["coordinates"]["coordinates"][1]:
            x = info_json["doc"]["coordinates"]["coordinates"][0]
            y = info_json["doc"]["coordinates"]["coordinates"][1]
            tags_list = info_json["doc"]["entities"]["hashtags"]
            if x and y:
                location = checkLocation.getLocation(x, y)
                if location:
                    numberCounter.append(location)
                    if tags_list:
                        for tags in tags_list:
                            if location not in tags_dict.keys():
                                tags_dict[location] = [tags["text"].lower()]
                            else:
                                tags_dict[location].append(tags["text"].lower())

countNumber = Counter(numberCounter)
for key, value in countNumber.most_common():
    print(str(key) + ": " + str(value) + " posts,")
print("Down to the square with the least number of posts;")
print()
for key in tags_dict:
    tagCounter = Counter(tags_dict[key]).most_common(5)
    print(str(key) + ": (", end=""),
    for key, value in tagCounter:
        print("(#" + str(key) + ", " + str(value) + "),", end=""),
    print(")")
print("Down to the top 5 hashtags in the grid cell with the least number of posts;")
end_time = time.time()
print(end_time - start_time)
