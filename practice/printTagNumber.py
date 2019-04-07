from collections import Counter


class printTagNumber:

    def __init__(self, tags_dict):
        self.tags_dict = tags_dict

    def countTopFive(self, tagCounter):
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

    def printIt(self):
        for key in self.tags_dict:
            tagCounter = Counter(self.tags_dict[key]).most_common()
            list_topFive = self.countTopFive(tagCounter)
            print(str(key) + ": (", end="")
            for info in list_topFive[0: len(list_topFive) - 1]:
                print("(" + str(info[0]) + "," + str(info[1]) + "),", end="")
            print("(" + str(list_topFive[-1][0]) + ", " + str(list_topFive[-1][1]) + "))")

