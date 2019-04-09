from ReadGrid import readingGrid


class checkLocation:

    def __init__(self):
        tempo = readingGrid()
        tempo.readLocation()
        self.dict_location_list = tempo.dict_location_list

    def getLocation(self, x, y):
        for dict_location in self.dict_location_list:
            for key in dict_location:
                if dict_location[key][0][0] <= x <= dict_location[key][0][1] and dict_location[key][1][0] <= y <= dict_location[key][1][1]:
                    return key
