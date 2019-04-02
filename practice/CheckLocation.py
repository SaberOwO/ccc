from ReadGrid import readingGrid


class checkLocation:

    def __init__(self):
        tempo = readingGrid()
        tempo.readLocation()
        self.dict_location = tempo.dict_location

    def getLocation(self, x, y):
        for key in self.dict_location:
            if self.dict_location[key][0][0] <= x <= self.dict_location[key][0][1] and self.dict_location[key][1][0] <= y <= self.dict_location[key][1][1]:
                return key
