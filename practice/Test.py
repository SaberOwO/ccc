from mpi4py import MPI
import json
from collections import Counter

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()
count = 0
package = []
testingData = [[1, 2], [3, 4], [1, 6], [7, 8], [9, 10], [10, 11],[112, 113], [111, 110]]
tagNum = 0
hehe = []
rank1 = 1
finallyList=[]


dict1 = {"a": "1", "b": "1"}
dict2 = {"a": "2", "b": "1"}
from collections import Counter
X,Y=Counter(dict1),Counter(dict2)
z=dict(X+Y)


#
# if comm_rank == 0:
#     for infos in testingData:
#         for info in infos:
#             package.append(info)
#         if len(package) == 4:
#             comm.send(package, dest=rank1%comm_size)
#             rank1 = rank1 + 1
#             if rank1 == comm_size:
#                 rank1 = 1
#             package.clear()
#     comm.send(package, dest=1)
#     flag = False
#     for i in range(1, comm_size):
#         comm.send(flag, dest=i)
#
# if comm_rank > 0:
#     while(True):
#         data_recv = comm.recv(source=0)
#         if data_recv == False:
#             break
#         for info in data_recv:
#             hehe.append(info)
# print("my rank is %d, I received :" % comm_rank)
# newData = comm.gather(hehe, root = 0)
# if comm_rank == 0:
#     for infos in newData:
#         for info in infos:
#             cyx.append(info)
#     print(cyx)


#
# if comm_rank == 0:
#
#     with open("resources/tinyTwitter(3).json", encoding='UTF-8') as twitter:
#         for line in twitter:
#             if line[2: 4] != "id":
#                 continue
#             if line[-2] == ",":
#                 line = line[:-2]
#             package.append(json.loads(line)["id"])
#             if len(package) == 4:
#                 comm.send(package, dest=rank1 % comm_size)
#                 rank1 = rank1 + 1
#                 if rank1 == comm_size:
#                     rank1 = 1
#                 package.clear()
#     comm.send(package, dest=1)
#     flag = False
#     for i in range(1, comm_size):
#         comm.send(flag, dest=i)
#
#
#
#
# if comm_rank > 0:
#     while(True):
#         data_recv = comm.recv(source=0)
#         if data_recv == False:
#             break
#         for line in data_recv:
#             hehe.append(line)
#
# newData = comm.gather(hehe, root=0)
#
# if comm_rank == 0:
#     for i in range(1, comm_size):
#         for info in newData[i]:
#             finallyList.append(info)
#     print(finallyList)


# if comm_rank == 0:
#     print("-" * 100)
#     for infos in newData:
#         for info in infos:
#             finallyList.append(info)
#             count += 1
#     print(finallyList)
#     print(count)



















# if comm_rank == 0:
#     while(flag):
#         if flag ==  0:
#             break
#         for id in comm.gather(hehe, root=0):
#             print("my rank is %d, I received :" % comm_rank)
#             hehe.append(id)
#             print(hehe)


# hehe = []


# def sendSomething(package):
#     if comm_rank == 0:
#         data = package
#     else:
#         data = None
#     data = comm.scatter(data, root=0)
#     return data
#
#
# for list_1 in testingData:
#     package.append(list_1)
#     if len(package) == 4:
#         newData = comm.gather(sendSomething(package), root=0)
#         print("my rank is %d, and I received:" % comm_rank)
#         if comm_rank == 0:
#             for element in newData:
#                 hehe.append(element)
#         package.clear()
#
#
# if comm_rank == 0:
#     print(hehe)

# import mpi4py.MPI as MPI
# comm = MPI.COMM_WORLD
# comm_rank = comm.Get_rank()
# comm_size = comm.Get_size()
#
# data_send = [comm_rank] * 4
# comm.send(data_send, dest=(comm_rank+1) % comm_size)
# data_recv = comm.recv(source=0)
# print("my rank is %d, I received :" % comm_rank)
# print(data_recv)
