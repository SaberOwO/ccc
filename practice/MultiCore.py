import mpi4py.MPI as MPI
import json
from CheckLocation import checkLocation
from printTwitterNumber import printTwitterNumber
from printTagNumber import printTagNumber
import time


comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()
package = []
numberCounter = []
tags_dict = {}
rank1 = 1
numberCounterList = []
tags_dictFinal = {}


# This method is used to search the tags inside text
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


# The rank 0 is main core as manager. It will read the json file and send the information
# to other worker.
if comm_rank == 0:
    start_time = time.time()
    with open("resources/tinyTwitter(3).json", "r", encoding="utf-8") as twitter:
        for line in twitter:
            package.append(line)
            if len(package) == 10:
                comm.send(package, dest=rank1, tag=3)
                rank1 = rank1 + 1
                if rank1 == comm_size:
                    rank1 = 1
                package.clear()
    comm.send(package, dest=1, tag=3)
    flag = False
    for i in range(1, comm_size):
        comm.send(flag, dest=i, tag=3)

# Other cores called worker receive the information and put the tags, which are from same grid
# into one list and encapsulate it into a dictionary. Also, it will return a list with each twitter's
# location
if comm_rank > 0:
    checkLocation = checkLocation()
    while True:
        data_recv = comm.recv(source=0, tag=3)
        if data_recv == False:
            break
        for info in data_recv:
            if info[2: 4] != "id":
                continue
            if info[-2] == ",":
                info = info[:-2]
            info_json = json.loads(info)
            if info_json["doc"]["coordinates"]:
                x = info_json["doc"]["coordinates"]["coordinates"][0]
                y = info_json["doc"]["coordinates"]["coordinates"][1]
            elif info_json["doc"]["geo"]:
                x = info_json["doc"]["geo"]["coordinates"][1]
                y = info_json["doc"]["geo"]["coordinates"][0]
            else:
                continue
            text = info_json["doc"]["text"]
            if x and y:
                location = checkLocation.getLocation(x, y)
                if location:
                    numberCounter.append(location)
                    searchTags(text, location)

newNumberCounter = comm.gather(numberCounter, root=0)
newTags_dict = comm.gather(tags_dict, root=0)

# At last manager will gather all the data from workers. And it will count the data and print out the results.
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
    print("total time: " + str(end_time - start_time))
