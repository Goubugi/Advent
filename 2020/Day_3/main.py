f = open('input.txt')
data = f.readlines()

horizontalCount = 0

numTrees = 0
dataSplit = []

for row in data:
    dataSplit.append(list(row)[:-1])

dataLen = len(dataSplit[0])

for row in dataSplit:
    if row[horizontalCount] == '#':
        numTrees = numTrees+1
    if horizontalCount == (dataLen - 3):
        horizontalCount = 0
    elif horizontalCount == (dataLen - 2):
        horizontalCount = 1
    elif horizontalCount == (dataLen - 1):
        horizontalCount = 2
    else:
        horizontalCount = horizontalCount + 3

print(numTrees)
