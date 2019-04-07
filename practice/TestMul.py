import mpi4py.MPI as MPI
import json
from contextlib import suppress
from CheckLocation import checkLocation
from printTwitterNumber import printTwitterNumber
from printTagNumber import printTagNumber
import time

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

numberCounter = []
tags_dict = {}
checkLocation = checkLocation()
package = []
rank1 = 1
numberCounterList = []
tags_dictFinal = {}

if comm_rank == 0:
    start_time = time.time()


def countTopFive(tagCounter):
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


def searchTags(text, location):
    start = 1
    end = -1
    word_list = text.split()
    if text[0] == " ":
        start = 0
    if text[-1] == " ":
        end = len(word_list)
    for word in word_list[start: end]:
        if word[0] == "#":
            if location not in tags_dict.keys():
                tags_dict[location] = [word.lower()]
            else:
                tags_dict[location].append(word.lower())


with open("resources/tinyTwitter(3).json") as twitter:
    for line in twitter:
        if line[2: 4] != "id":
            continue
        if line[-2] == ",":
            line = line[:-2]
        info_json = json.loads(line)
        with suppress(Exception):
            x = info_json["doc"]["coordinates"]["coordinates"][0]
            y = info_json["doc"]["coordinates"]["coordinates"][1]
            text = info_json["doc"]["text"]
            if x and y:
                location = checkLocation.getLocation(x, y)
                if location:
                    numberCounter.append(location)
                    searchTags(text, location)

newNumberCounter = comm.gather(numberCounter, root=0)
newTags_dict = comm.gather(tags_dict, root=0)


if comm_rank == 0:
    for i in range(1, comm_size):
        for info in newNumberCounter[i]:
            numberCounterList.append(info)
    TwitterNumber = printTwitterNumber(numberCounterList)
    TwitterNumber.printIt()
    for i in range(1, comm_size):
        for key in newTags_dict[i]:
            if key in tags_dictFinal.keys():
                for value in newTags_dict[i][key]:
                    tags_dictFinal[key].append(value)
            else:
                tags_dictFinal[key] = []
                for value in newTags_dict[i][key]:
                    tags_dictFinal[key].append(value)
    TagNumber = printTagNumber(tags_dictFinal)
    TagNumber.printIt()
    end_time = time.time()
    print(end_time-start_time)
