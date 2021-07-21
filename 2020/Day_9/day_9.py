f = open('input.txt')
data = f.readlines()
partOne = False

def findPreamble(index, input_data, preamble):
    i = 1
    ret_list = []
    while i <= preamble:
        foundNum = input_data[index-i]
        if foundNum.find('\n') != -1:
            foundNum = foundNum[:-1]
        foundNum = int(foundNum)
        ret_list.append(foundNum)
        i+=1
    return ret_list

def visualizeDictionary(dict):
    for key in dict.keys():
        print(key, ':', dict[key])


def parseNewData(input_data, preamble):
    index = 0
    newData = {}
    for row in input_data:
        if index >= preamble:
            if row.find('\n') != -1:
                num = int(row[:-1])
                immediate_preamble = findPreamble(index, input_data, preamble)
            else:
                num = int(row)
                immediate_preamble = findPreamble(index, input_data, preamble)
            newData.update({index:{'num':num,'preamble':immediate_preamble}})
        index+=1
    return newData

def isSumFunc(num,l):
    index = 0
    secondIndex = 1
    while index < len(l):
        while secondIndex < (len(l)):
            numOne = l[index]
            numTwo = l[secondIndex]
            if (numOne + numTwo) == num:
                return True
            secondIndex+=1
        index+=1
        secondIndex = index+1

    return False

def findFirstNum(newData):
    for key in newData.keys():
        data = newData[key]
        isSum = isSumFunc(data['num'],data['preamble'])
        if not isSum:
            return data['num']

def parseListData(input_data):
    newList = []
    for row in input_data:
        if row.find('\n') != -1:
            newRow = int(row[:-1])
        else:
            newRow = int(row)
        newList.append(newRow)
    return newList


def findconsecList(num, listData):
    for row in listData:
        l = []
        count = 0
        index = listData.index(row)
        while count <= num:
            iterNum = listData[index]
            l.append(iterNum)
            count+=iterNum
            index+=1
            if count == num:
                return l





newData = parseNewData(data,25)
firstNum = findFirstNum(newData)
if partOne:
    print(f'The first num not a sum of preamble is: {firstNum}')
else:
    listData = parseListData(data)
    consecutiveList = findconsecList(firstNum, listData)
    max = max(consecutiveList)
    min = min(consecutiveList)
    weakness = max+min
    print(f'The encryption weakness is: {weakness}')
