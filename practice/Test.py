from collections import Counter

count = Counter("nfgianbioabngowengornijsrbisuhbnofajjgonigrbuiornampamoanfgoengufrnge").most_common()
print(count)
tempo = count[0][1]
counter = 1
list_1 = []
for k, v in count:
    if tempo > v:
        tempo = v
        counter = counter + 1
    if counter > 5:
        break
    list_1.append([k, v])
print(list_1)
print(list_1[0:len(list_1) - 1])
for info in list_1[0:len(list_1) - 1]:
    print(info[0])
    print(info[1])

