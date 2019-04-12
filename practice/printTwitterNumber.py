from collections import Counter

# This class is used to print the total twitter in each grid
class printTwitterNumber:

    def __init__(self, numberCounter):
        self.countNumber = Counter(numberCounter)

    def printIt(self):
        for key, value in self.countNumber.most_common():
            print(str(key) + ": " + str(value) + " posts,")
        print()