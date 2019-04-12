from ReadGrid import readingGrid

# This class is used to get the location of melbourne, which is divided by grid.
class checkLocation:

    def __init__(self):
        tempo = readingGrid()
        tempo.readLocation()
        self.dict_location_list = tempo.dict_location_list


    # This method will recieve two parameters, which represent the x and y in coordinates.
    # It will return the grid number of that point.
    def getLocation(self, x, y):
        for i in range(0, len(self.dict_location_list)):
            for key in self.dict_location_list[i]:
                if self.dict_location_list[i][key][0][0] <= x <= self.dict_location_list[i][key][0][1] and \
                        self.dict_location_list[i][key][1][0] <= y <= self.dict_location_list[i][key][1][1]:
                    return key
