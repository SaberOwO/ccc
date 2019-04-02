from collections import Counter
from ReadTwitter import readTwitter

readTwitter = readTwitter()
readTwitter.readingInfo()
countNumber = Counter(readTwitter.numberCounter)
for key, value in countNumber.most_common():
    print(str(key) + ": " + str(value) + " posts,")
print("Down to the square with the least number of posts;")
print()
for key in readTwitter.tags_dict:
    tagCounter = Counter(readTwitter.tags_dict[key]).most_common(5)
    print(str(key) + ": (", end=""),
    for key, value in tagCounter:
        print("(#" + str(key) + ", " + str(value) + "),", end=""),
    print(")")
print("Down to the top 5 hashtags in the grid cell with the least number of posts;")
/Users/xinyanhuang/PycharmProjects/practice/resources/tinyTwitter(3).json