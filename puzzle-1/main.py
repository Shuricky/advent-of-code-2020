def readFile():
    listOfNum = []
    with open("listOfNum") as fp:
        for line in fp:
            listOfNum.append(int(line.strip('\n')))
    return listOfNum

def puzzle1(listOfNum):
    listOfNumSet = set(listOfNum)
    for i in listOfNumSet:
        if 2020 - i in listOfNumSet:
            print("Part 1: " + str(i * (2020 - i)))
            return

def puzzle2(listOfNum):
    listOfNumSet = set(listOfNum)
    for i in listOfNumSet:
        for j in listOfNumSet:
            if 2020 - i - j in listOfNumSet:
                print("Part 2: " + str((2020 - i - j) * i * j))
                return

if __name__ == "__main__":
    listOfNum = readFile()
    puzzle1(listOfNum)
    puzzle2(listOfNum)