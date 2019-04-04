import json
# read the melbGrid.json and put the location data into a dictionary
class readingGrid:

    def __init__(self):
        self.dict_location = {}
        with open('resources/melbGrid.json') as grib:
            tempo = json.loads(grib.read())
        self.location_info = tempo["features"]

    def readLocation(self):
        for list in self.location_info:
            name = list["properties"]["id"]
            xRange = (list["properties"]["xmin"], list["properties"]["xmax"])
            yRange = (list["properties"]["ymin"], list["properties"]["ymax"])
            self.dict_location[name] = (xRange, yRange)
