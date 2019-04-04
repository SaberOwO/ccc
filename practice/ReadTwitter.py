import json

from CheckLocation import checkLocation


class readTwitter:

    def __init__(self):
        self.checkLocation = checkLocation()
        with open('resources/bigTwitter.json') as f:
            json_dict = json.loads(f.read())
        self.json_context = json_dict["rows"]
        self.numberCounter = []
        self.tags_dict = {}

    def readingInfo(self):
        for info in self.json_context:
            x = info["value"]["geometry"]["coordinates"][0]
            y = info["value"]["geometry"]["coordinates"][1]
            tags_list = info["doc"]["entities"]["hashtags"]
            if x and y:
                location = self.checkLocation.getLocation(x, y)
                if location:
                    self.numberCounter.append(location)
                if tags_list and location:
                    for tags in tags_list:
                        if location not in self.tags_dict.keys():
                            self.tags_dict[location] = [tags["text"].lower()]
                        else:
                            self.tags_dict[location].append(tags["text"].lower())
