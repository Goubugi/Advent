f = open('input.txt')
data = f.readlines()

def parseData(input):
   newData = []
   for row in input:
       if '\n' in row:
           r = row[:-1]
           r = [character for sublist in r for character in sublist]
       else:
           r = [character for sublist in row for character in sublist]
       newData.append(r)
   return newData

def viewSeating(input):
    for i in input:
        print(i)

def getSurrounding(row,col,input):
    retList = []
    leftMost = False
    rightMost = False
    upper = False
    bottom = False
    if col==0:
        leftMost = True
    if col == len(input[0])-1:
        rightMost = True
    if row == len(input)-1:
        bottom = True
    if row == 0:
        upper = True

    if upper:
        if leftMost:
            retList = [input[row][col+1],input[row+1][col+1],input[row+1][col]]
        elif rightMost:
            retList = [input[row][col-1],input[row+1][col-1],input[row+1][col]]
        else:
            retList = [input[row][col - 1], input[row + 1][col - 1], input[row + 1][col], input[row][col+1],input[row+1][col+1]]
    elif bottom:
        if leftMost:
            retList = [input[row][col+1],input[row-1][col+1],input[row-1][col]]
        elif rightMost:
            retList = [input[row][col-1],input[row-1][col-1],input[row-1][col]]
        else:
            retList = [input[row][col - 1], input[row - 1][col - 1], input[row - 1][col], input[row][col+1],input[row-1][col+1]]
    elif leftMost:
        retList = [input[row-1][col], input[row - 1][col + 1], input[row][col+1], input[row+1][col + 1],
                input[row + 1][col]]
    elif rightMost:
        retList = [input[row-1][col], input[row - 1][col - 1], input[row][col-1], input[row+1][col - 1],
                input[row + 1][col]]
    else:
        retList = [input[row-1][col+1], input[row-1][col],input[row-1][col-1],input[row+1][col+1],input[row+1][col],input[row+1][col-1],input[row][col+1],input[row][col-1],]
    return retList

def countSeat(l):
    numOcc = 0
    numEmpty = 0
    for i in l:
        if i == '#':
            numOcc+=1
        elif i == 'L':
            numEmpty+=1
    return numOcc,numEmpty




def updateSeating(input):
    newMap = [[0 for i in range(len(input[0]))] for j in range(len(input))]
    dim1 = len(newMap)
    dim2 = len(newMap[0])

    for row in range(len(input)):
        for seat in range(len(input[row])):
            surrounding = getSurrounding(row,seat,input)
            numOcc,numEmpty = countSeat(surrounding)
            if input[row][seat] == '.':
                newMap[row][seat] = '.'
            elif input[row][seat] == '#' and numOcc >= 4:
                newMap[row][seat] = 'L'
            elif input[row][seat] == 'L' and numOcc == 0:
                newMap[row][seat] = '#'
            else:
                newMap[row][seat] = input[row][seat]
    return newMap

def findRepetition(input):
    previousState = []
    modified = input.copy()
    while True:
        if previousState == modified:
            return modified
        previousState = modified
        modified = updateSeating(modified)

def countOccupied(input):
    count=0
    for i in input:
        for j in i:
            if j == '#':
                count+=1
    return count



newData = parseData(data)
repeatedState = findRepetition(newData)
count = countOccupied(repeatedState)
print(count)

