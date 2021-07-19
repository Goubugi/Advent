f = open('input.txt')
data = f.readlines()
dataSplit = []
for row in data:
    i = list(row)
    if i[-1] == '\n':
        i = i[:-1]
    dataSplit.append(i)

dataLen = len(dataSplit[0])

def DownOne(numRight):
    numTrees = 0
    horizontalCount = 0
    for row in dataSplit:
        if row[horizontalCount] == '#':
            numTrees = numTrees + 1
        if horizontalCount+numRight >= dataLen:
            horizontalCount = horizontalCount+numRight - dataLen
        else:
            horizontalCount = horizontalCount + numRight
    return numTrees

def DownTwo(numRight):
    checkRow = True
    numTrees = 0
    horizontalCount = 0
    for row in dataSplit:
        if checkRow:
            if row[horizontalCount] == '#':
                numTrees = numTrees + 1
            if horizontalCount + numRight >= dataLen:
                horizontalCount = horizontalCount + numRight - dataLen
            else:
                horizontalCount = horizontalCount + numRight
        checkRow = not checkRow

    return numTrees
total = DownOne(1)*DownOne(3)*DownOne(5)*DownOne(7)*DownTwo(1)
print(f'The total is {total}')





