import json
# read the melbGrid.json and put the location data into a dictionary
class readingGrid:

    def __init__(self):
        self.dict_location_list = []
        with open('resources/melbGrid(1).json') as grib:
            tempo = json.loads(grib.read())
        self.location_info = tempo["features"]

    def readLocation(self):
        for list in self.location_info:
            dict_location = {}
            name = list["properties"]["id"]
            xRange = (list["properties"]["xmin"], list["properties"]["xmax"])
            yRange = (list["properties"]["ymin"], list["properties"]["ymax"])
            dict_location[name] = (xRange, yRange)
            self.dict_location_list.append(dict_location)

