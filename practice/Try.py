import json
from contextlib import suppress
count = 0
with open('resources/tinyTwitter(3).json') as f:
        a = f.readlines(100)
        for sentence in a:
            print(sentence)
            count += 1

print(count)