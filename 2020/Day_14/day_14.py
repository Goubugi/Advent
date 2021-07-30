f = open('input.txt')
data = f.readlines()
mem = {}
partOne = False

def parseData(data):
    ret = []
    for i in data:
        if '\n' in i:
            ret.append(i[:-1])
        else:
            ret.append(i)
    return ret

def convertToBit(row):
    return "{:036b}".format(row)

def convertToInt(bit):
    return int(bit,2)

def findSums(data):
    mask = 0
    for row in data:
        if 'mask' in row:
            mask = row[row.find('=')+2:]
        else:
            key = row[row.find('[')+1:row.find(']')]
            value = convertToBit(int(row[row.find('=')+2:]))
            index = 0
            retValue = ''
            for i in value:
                if mask[index]=='X':
                    retValue+=(value[index])
                else:
                    retValue+=(mask[index])

                index+=1
            mem[key] = convertToInt(retValue)
    ret = 0
    for key in mem.keys():
        ret+=mem[key]
    return ret

def recordMemory(count,val):
    memList = []
    num = val.count('X')
    for i in range(2**num):
        copy = val
        x = "{:036b}".format(i)
        x = x[-num:]
        replace = [n for n in x]
        for i in replace:
            copy = copy.replace('X',i,1)
        memList.append(convertToInt(copy))
    for i in memList:
        mem[i] = count





def findSums2(data):
    mask = 0
    for row in data:
        if 'mask' in row:
            mask = row[row.find('=')+2:]
        else:
            memory = int(row[row.find('[')+1:row.find(']')])
            memoryValue = convertToBit(memory)
            countValue = int(row[row.find('=')+2:])
            index = 0
            retValue = ''
            for i in memoryValue:
                x = mask[index]
                if mask[index]=='X':
                    retValue+=('X')
                elif mask[index]=='1':
                    retValue+='1'
                else:
                    retValue+=(i)
                index+=1

            recordMemory(countValue,retValue)
    ret = 0
    for key in mem.keys():
        ret+=mem[key]
    return ret

if partOne:
    newData = parseData(data)
    answer1 = findSums(newData)
    print(answer1)
else:
    newData = parseData(data)
    answer2 = findSums2(newData)
    print(answer2)
