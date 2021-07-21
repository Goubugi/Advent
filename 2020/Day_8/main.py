import copy

f = open('input.txt')
data = f.readlines()
partOne = False

def parseNewData(data):
    newData = {}
    index = 0
    for row in data:
        if row.find('\n')!=-1:
            action = row[0:3]
            type = row[4]
            num = int(row[5:-1])
        else:
            action = row[0:3]
            type = row[4]
            num = int(row[5:])
        newData.update({index:{'count':0,'action':action,'type':type,'num':num}})
        index+=1
    return newData

def visualizeDictionary(dict):
    for key in dict.keys():
        print(key, ':', dict[key])

def countAcc(inputDict):
    count = 0
    index = 0
    while True:
        info = inputDict[index]
        if info['count'] != 0:
            return count
        info['count']+=1
        if info['action'] == 'nop':
            index+=1
        elif info['action'] == 'acc':
            if info['type'] == '+':
                count+=info['num']
                index += 1
            else:
                count-=info['num']
                index += 1
        elif info['action'] == 'jmp':
            if info['type'] == '+':
                index+=info['num']
            else:
                index-=info['num']

def testCountability(dict):
    count = 0
    index = 0
    newDict = copy.deepcopy(dict)
    while True:
        if index == len(newDict.keys()):
            return count
        data = newDict[index]
        if data['count'] != 0:
            return -1
        data['count']+=1
        if data['action'] == 'nop':
            index+=1
        elif data['action'] == 'acc':
            if data['type'] == '+':
                count+=data['num']
                index += 1
            else:
                count-=data['num']
                index += 1
        elif data['action'] == 'jmp':
            if data['type'] == '+':
                index+=data['num']
            else:
                index-=data['num']

def newCountAcc(inputDict):
    for key in inputDict.keys():
        info = inputDict[key]
        if info['action'] != 'acc':
            newInfo = dict(info)
            if info['action'] == 'nop':
                newInfo.update({'action':'jmp'})
            else:
                newInfo.update({'action':'nop'})
            tempDict = dict(inputDict)
            tempDict.update({key:newInfo})
            count = testCountability(tempDict)
            if count != -1:
                return count


newData = parseNewData(data)
if partOne:
    count = countAcc(newData)
    print(f'The value of the accumulator variable is: {count}')
else:
    count = newCountAcc(newData)
    print(f'The value of the accumulator variable after termination is: {count}')
