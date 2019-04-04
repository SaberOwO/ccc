# import json
#
# from CheckLocation import checkLocation
#
#
# class readTwitter:
#
#     def __init__(self):
#         self.checkLocation = checkLocation()
#         with open('resources/tinyTwitter(3).json') as f:
#             json_dict = json.loads(f.readline())
#         self.json_context = json_dict["rows"]
#         self.numberCounter = []
#         self.tags_dict = {}
#
#     def readingInfo(self):
#         for info in self.json_context:
#             x = info["value"]["geometry"]["coordinates"][0]
#             y = info["value"]["geometry"]["coordinates"][1]
#             tags_list = info["doc"]["entities"]["hashtags"]
#             if x and y:
#                 location = self.checkLocation.getLocation(x, y)
#                 if location:
#                     self.numberCounter.append(location)
#                 if tags_list and location:
#                     for tags in tags_list:
#                         if location not in self.tags_dict.keys():
#                             self.tags_dict[location] = [tags["text"].lower()]
#                         else:
#                             self.tags_dict[location].append(tags["text"].lower())
#144.92340088,-37.95935781
import json

with open("resources/tinyTwitter(3).json") as f:
    for line in f:
        if line[2: 4] != "id":
            continue
        if line[-2] == ",":
            line = line[:-2]
        info_json = json.loads(line)
        x = info_json["doc"]["coordinates"]["coordinates"][0]
        y = info_json["doc"]["coordinates"]["coordinates"][1]
        print(str(x) + ", " + str(y))