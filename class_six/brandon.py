f = open("rank.txt", "w+")
f.write("1 2\n")
for i in range(2):
    f.write('1 1\n')
f.write("1 2\n")
f.close()

h = 0
newList = []

with open("rank.txt", "r") as fin:
    fin = fin.read()
    list = (list(fin.replace(' ', '\n')))
print(list)

f = open("calc.txt", "w+")
for i in list:
    f.write(list[h])
    h = h + 1
f.close()

h = 0
with open("calc.txt", "r") as new:
    new = new.readlines()
    for line in new:
        oof = (line.strip())
        newList.insert(h, int(oof))
        h = h + 1
    print(newList)

listLength = (len(newList) / 2)


anotherList = []

def check():
    global listLength
    global anotherList
    global newList
    if listLength == 4:
        for i in range((int(listLength) - 1)):
            e = (((int(newList[int(listLength)]) - 0) * 2) + ((int(newList[int(listLength)]) - 1) * 2)) / 2
            listLength = 0
            print(e)
            anotherList.append(int(e))
            for i in range((int(listLength) - 1)):
                e = (((int(newList[int(listLength)]) - 2) * 2) + ((int(newList[int(listLength)]) - 3) * 2)) / 2
                listLength = 0
                print(e)
                anotherList.append(int(e))
                for i in range((int(listLength) - 1)):
                    e = (((int(newList[int(listLength)]) - 4) * 2) + ((int(newList[int(listLength)]) - 5) * 2)) / 2
                    listLength = 0
                    print(e)
                    anotherList.append(int(e))

check()
listLength = listLength - 1

print(anotherList)

print("Promoted from gold to platinum: %s person(s)" % anotherList[0])
print("Promoted from silver to gold: %s person(s)" % anotherList[1])
print("Promoted from bronze to silver: %s person(s)" % anotherList[2])