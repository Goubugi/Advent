import numpy as np
import pandas as pd
import math


def scanData(input):
    f = open(input)

    tileNames = list()

    def filter(string):
        ret = []
        for i in string:
            if i.isnumeric():
                ret.append(i)

        return "".join(ret)

    def token(string):
        ret = []
        for i in string:
            if i != '\n':
                ret.append(i)

        return ret

    df = pd.DataFrame()

    for i in f:
        if 'Tile' in i:
            tileNames.append(filter(i))
            pass
        elif i != '\n':
            df = df.append(token(i))

    data = np.array(df[0])
    numTiles = len(tileNames)
    data = (data.reshape(numTiles, 10, 10))

    ret = {}
    index = 0
    for i in tileNames:
        ret.update({i: pd.DataFrame(data[index])})
        index = index + 1

    return ret

def getBound(df):
    top = df.iloc[0].tolist()
    bottom = df.iloc[9].tolist()
    left = df[0].tolist()
    right = df[9].tolist()
    topF = top.copy()
    topF.reverse()
    bottomF = bottom.copy()
    bottomF.reverse()
    leftF = left.copy()
    leftF.reverse()
    rightF = right.copy()
    rightF.reverse()

    return top,bottom,left,right,topF,bottomF,leftF,rightF

def Match(t,b,l,r,top,bottom,left,right):
    if t==bottom:
        return "Above"
    elif b==top:
        return "Bottom"
    elif l==right :
        return "Left"
    elif r ==left:
        return "Right"
    else:
        return ""

def unFlip(df):
    ret = (df.iloc[::-1])
    return pd.DataFrame(ret.to_numpy())

def rotate(df):
    return pd.DataFrame(unFlip(df.T).to_numpy())

def findBorder(d,key):
    copy = d.copy()
    copy.pop(key)
    ret = {}
    t, b, l, r, tf,bf,lf,rf = getBound(d[key])
    for i in copy.keys():
        top, bottom, left, right, topF, bottomF, leftF, rightF = getBound(copy[i])
        norm = [top,bottom,left,right]
        flip = [topF, bottomF, leftF, rightF]
        combined = norm+flip
        if(t in combined )|( b in combined )| (l in combined )|( r in combined):
            tryFlip = True
            #isFlipped = (t in flip )|( b in flip )|( l in flip )|( r in flip) | (t==top) | (r == right) | (l == left) | (b==bottom)
           # if (t in flip ) & (b in flip) & (l in flip) & (r in flip):
            #    isFlipped = False
            for loop in range(4):
                if (Match(t, b, l, r, top, bottom, left, right) == ""):
                    copy.update({i: rotate(copy[i])})
                    top, bottom, left, right, topF, bottomF, leftF, rightF = getBound(copy[i])
                else:
                    tryFlip=False
                    break
            if(tryFlip):
                copy.update({i:unFlip(copy[i])})
                top, bottom, left, right, topF, bottomF, leftF, rightF = getBound(copy[i])
                for n in range(4):
                    if(Match(t,b,l,r,top,bottom,left,right)==""):
                        copy.update({i: rotate(copy[i])})
                        top, bottom, left, right, topF, bottomF, leftF, rightF = getBound(copy[i])
                    else:
                        break

        ret.update({i:Match(t,b,l,r,top,bottom,left,right)})
    return ret,copy
    pass

def setupDict(input):
    ret = {}
    for i in input.keys():
        ret.update({i:False})
    return ret

def recursiveTrace( tileKey, input, initial):
    if(recursiveDict[tileKey]==True):
        return
    if(initial==True):
        tupleDict.update({tileKey:(0,0)})
    relation,update = findBorder(input,tileKey)
    relationDict.update({tileKey:relation})
    recursiveDict.update({tileKey:True})
    input.update(update)
    NearbyTiles = []
    for i in relation.keys():
        if relation[i] != '':
            NearbyTiles.append(i)
    for j in NearbyTiles:
        if (j in tupleDict.keys()) == False:
            if relation[j] == 'Left':
                tupleDict.update({j:(tupleDict[tileKey][0]-1,tupleDict[tileKey][1])})
            if relation[j] == 'Right':
                tupleDict.update({j: (tupleDict[tileKey][0] + 1, tupleDict[tileKey][1])})
            if relation[j] == 'Above':
                tupleDict.update({j: (tupleDict[tileKey][0], tupleDict[tileKey][1]+1)})
            if relation[j] == 'Bottom':
                tupleDict.update({j: (tupleDict[tileKey][0], tupleDict[tileKey][1]-1)})

        recursiveTrace(tileKey=j,input = input, initial = False)

    return input

def findOrder():
    smallestX = 0
    largestY = 0
    for i in tupleDict.keys():
        if (tupleDict[i][0] < smallestX):
            smallestX = tupleDict[i][0]
        if (tupleDict[i][1] > largestY):
            largestY = tupleDict[i][1]


    list = []

    outerIndex = 0
    for i in range(length):
        innerIndex = 0
        for j in range(length):
            for k in tupleDict.keys():
                if (tupleDict[k] == (smallestX + innerIndex, largestY - outerIndex)):
                    list.append(k)
            innerIndex = innerIndex + 1
        outerIndex = outerIndex + 1
    numpy = np.array(list)
    numpy = numpy.reshape(length, length)
    return numpy


data = scanData('sample.txt')

input = data.copy()
recursiveDict = setupDict(input)
relationDict = {}
tupleDict = {}

finalImage = recursiveTrace(tileKey=str(list(data.keys())[0]),input=data, initial=True)
length = int(math.sqrt(len(data)))
finalOrder = findOrder()
fourCorners = [finalOrder[0,0],finalOrder[0,length-1],finalOrder[length-1,0],finalOrder[length-1,length-1]]


df = pd.DataFrame()
for i in finalOrder:
    listOfDf = []
    for j in i:
        listOfDf.append(finalImage[j])
    temp = pd.concat(listOfDf,axis = 1)
    df = pd.concat([df,temp],axis = 0)

df.columns =  [i for i in range(length*10)]
df.index =  [i for i in range(length*10)]
print(df)
npArray = df.to_numpy().flatten()
index = 0
numSM = 0
for i in npArray:
    if(index+2*(length*10) < len(npArray)):
        if(npArray[index]=='#'):
            if(npArray[index+(length*10)-18]=='#'):
                if(npArray[index+(length*10)-13]=='#'):
                    if (npArray[index+(length*10)-12] == '#'):
                        if (npArray[index+(length*10)-7] == '#'):
                            if (npArray[index + (length * 10) - 6] == '#'):
                                if (npArray[index + (length * 10) - 1] == '#'):
                                    if (npArray[index + (length * 10)] == '#'):
                                        if (npArray[index + (length * 10) +1] == '#'):
                                            if (npArray[index + 2*(length * 10) - 2] == '#'):
                                                if (npArray[index + 2*(length * 10) - 5] == '#'):
                                                    if (npArray[index + 2*(length * 10) - 8] == '#'):
                                                        if (npArray[index + 2*(length * 10) - 11] == '#'):
                                                            if (npArray[index + 2*(length * 10) - 14] == '#'):
                                                                if (npArray[index + 2*(length * 10) - 17] == '#'):
                                                                    numSM = numSM+1

    index = index +1

print(numSM)


#print(f'Four Corners are {fourCorners}')
#print(f'Final Ouput is {int(fourCorners[0])*int(fourCorners[1])*int(fourCorners[2])*int(fourCorners[3])}')












