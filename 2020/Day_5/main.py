f = open('input.txt')
data = f.readlines()
newData = []
partOne = False

for row in data:
    if row[-1] == '\n':
        newData.append(row[:-1])
    else:
        newData.append(row)

sanityCheckIDList = []

for boardingPass in newData:
    upperRow = 127
    lowerRow = 0
    upperCol = 7
    lowerCol = 0
    for i in boardingPass:
        if i == 'F':
            upperRow = (upperRow+1-lowerRow)/2 - 1 + lowerRow
        elif i == 'B':
            lowerRow = (upperRow+1-lowerRow)/2 + lowerRow
        if i == 'L':
            upperCol = (upperCol+1-lowerCol)/2 - 1 + lowerCol
        elif i == 'R':
            lowerCol = (upperCol+1-lowerCol)/2 + lowerCol
    sanityCheckIDList.append(int(upperRow*8+upperCol))

print(f'The max ID for sanity check is: {max(sanityCheckIDList)}')

def findSeatID(inputList):
    inputList.sort()
    index = 0
    for i in inputList:
        if index < (len(inputList) - 1):
            if inputList[index]+2 == inputList[index+1]:
                return inputList[index]+1
        index = index+1
    return None

mySeatID = findSeatID(sanityCheckIDList)
print(f'My seat ID is: {mySeatID}')



