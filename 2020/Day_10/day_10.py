from math import factorial
f = open('input.txt')
data = f.readlines()
partOne = False

def parseDataList(data):
    newData = []
    for row in data:
        if '\n' in row:
            r = row[:-1]
        else:
            r = row
        r = int(r)
        newData.append(r)
    return newData

def countDifferences(input):
    difOne = 1
    difTwo = 0
    difThree = 0
    for i in input:
        if i == input[-1]:
            difThree+=1
            return difOne*difThree
        index = input.index(i)
        if( input[index+1] - i) == 1:
            difOne+=1
        elif (input[index + 1] - i) == 1:
            difTwo += 1
        else:
            difThree += 1

def countOptionalAdapters(input):
    dictOptional = {}
    con = 0
    keys = 0
    previousOptional = False
    startNum = 0
    for i in input:
        index = input.index(i)
        before = 0
        if i != input[0]:
            before = input[index - 1]
        after = i + 3
        if i != input[-1]:
            after = input[index + 1]
        if (before + 3 == i) or (after - 3 == i) or (i == input[-1]): #Case for when it is essential
            if previousOptional== True: #End of a chain
                dictOptional.update({keys:{'consecutive':con,'Total Gap':i-startNum}})
                keys+=1 #Increment key to not overwrite past data
                con = 0
            previousOptional = False

        else: #Case for when it is nonessential
            con+=1
            if previousOptional == False: #Start of a chain
                if index - 1 == -1:
                    startNum = 0
                else:
                    startNum = input[index-1]
            previousOptional = True
        if i == input[-1]:
            return dictOptional


def nCr(n, r):
    return int(factorial(n)/(factorial(n-r)*factorial(r)))

def visualizeDictionary(dict):
    for key in dict.keys():
        print(key, ':', dict[key])

def calcPermute(dict):
    allSegments = []
    for key in dict.keys():
        data = dict[key]
        minimumInGap = int((data['Total Gap'])/3)
        sum = 0
        for i in range(data['consecutive']+1):
            if i >= minimumInGap:
                sum+=nCr(data['consecutive'],i)
        if data['Total Gap'] % 3 == 0:
            sum+=1
        allSegments.append(sum)
    totalSum = 1
    for i in allSegments:
        totalSum*=i
    return totalSum




if partOne:
    newData = parseDataList(data)
    newData.sort()
    count = countDifferences(newData)
    print(f'The difference in 3 and 1 multiplied is {count}')
if not partOne:
    newData = parseDataList(data)
    newData.sort()
    optional = countOptionalAdapters(newData)
    count = calcPermute(optional)
    print(count)


