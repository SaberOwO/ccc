from collections import Counter
class printTwitterNumber:

    def __init__(self, numberCounter):
        self.countNumber = Counter(numberCounter)

    def printIt(self):
        for key, value in self.countNumber.most_common():
            print(str(key) + ": " + str(value) + " posts,")
        print("Down to the square with the least number of posts;")
        print()