f = open('input.txt')
data = f.readlines()
partOne = False

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

def countViews(row,col,input,direction):

    if ((row == -1) or (col == -1) or (col ==  len(input[0])) or (row == len(input))):
        return 0,0
    elif input[row][col] == '#' and direction != 0:
        return 1,0
    elif input[row][col] == 'L' and direction != 0:
        return 0,1
    else:
        if direction == 1:
            numOccupied,numEmpty =  countViews(row-1,col,input,1)
            return numOccupied,numEmpty
        if direction == 2:
            numOccupied,numEmpty =  countViews(row-1,col+1,input,2)
            return numOccupied, numEmpty
        if direction == 3:
            numOccupied,numEmpty =  countViews(row,col+1,input,3)
            return numOccupied, numEmpty
        if direction == 4:
            numOccupied,numEmpty =  countViews(row+1,col+1,input,4)
            return numOccupied, numEmpty
        if direction == 5:
            numOccupied,numEmpty =  countViews(row+1,col,input,5)
            return numOccupied, numEmpty
        if direction == 6:
            numOccupied,numEmpty =  countViews(row+1,col-1,input,6)
            return numOccupied, numEmpty
        if direction == 7:
            numOccupied,numEmpty =  countViews(row,col-1,input,7)
            return numOccupied, numEmpty
        if direction == 8:
            numOccupied,numEmpty =  countViews(row-1,col-1,input,8)
            return numOccupied, numEmpty
    retOcc, retEmp = 0, 0
    numOccupied, numEmpty = countViews(row - 1, col, input, 1)
    retOcc, retEmp = retOcc+numOccupied,retEmp+numEmpty
    numOccupied, numEmpty = countViews(row - 1, col + 1, input, 2)
    retOcc, retEmp = retOcc+numOccupied,retEmp+numEmpty
    numOccupied, numEmpty = countViews(row, col + 1, input, 3)
    retOcc, retEmp = retOcc+numOccupied,retEmp+numEmpty
    numOccupied, numEmpty = countViews(row + 1, col + 1, input, 4)
    retOcc, retEmp = retOcc+numOccupied,retEmp+numEmpty
    numOccupied, numEmpty = countViews(row + 1, col, input, 5)
    retOcc, retEmp = retOcc+numOccupied,retEmp+numEmpty
    numOccupied, numEmpty = countViews(row + 1, col - 1, input, 6)
    retOcc, retEmp = retOcc+numOccupied,retEmp+numEmpty
    numOccupied, numEmpty = countViews(row, col - 1, input, 7)
    retOcc, retEmp = retOcc+numOccupied,retEmp+numEmpty
    numOccupied, numEmpty = countViews(row - 1, col - 1, input, 8)
    retOcc, retEmp = retOcc+numOccupied,retEmp+numEmpty
    return retOcc,retEmp











def updateSeatingTwo(input):
    newMap = [[0 for i in range(len(input[0]))] for j in range(len(input))]
    for row in range(len(input)):
        for seat in range(len(input[row])):
            numOcc,numEmpty = countViews(row,seat,input,0)
            if input[row][seat] == '.':
                newMap[row][seat] = '.'
            elif input[row][seat] == '#' and numOcc >= 5:
                newMap[row][seat] = 'L'
            elif input[row][seat] == 'L' and numOcc == 0:
                newMap[row][seat] = '#'
            else:
                newMap[row][seat] = input[row][seat]
    return newMap

def findRepetition(input):
    previousState = []
    modified = input.copy()
    if partOne:
        while True:
            if previousState == modified:
                return modified
            previousState = modified
            modified = updateSeating(modified)
    else:
        while True:
            if previousState == modified:
                return modified
            previousState = modified
            modified = updateSeatingTwo(modified)


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

