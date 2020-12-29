import numpy as np
import pandas as pd

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

    return ret,numTiles

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

def findBorder(key):
    copy = data.copy()
    copy.pop(key)
    related = []
    ret = {}
    t, b, l, r, tf, bf, lf, rf = getBound(data[key])
    for i in copy.keys():
        top, bottom, left, right, topF, bottomF, leftF, rightF = getBound(copy[i])
        combined = [top,bottom,left,right,topF,bottomF,leftF,rightF]
        if (t in combined) | (b in combined) | (l in combined) | (r in combined):
            related.append(i)

    ret.update({key:related})
    return ret
    pass

def findFirstCorner(data):

    for i in data.keys():
        if len(data[i])==2:
            return  i

def findRelations(Relations):
    for i in data.keys():
        matches = findBorder(i)
        Relations.update(matches)
    return Relations

data,Length = scanData('sample.txt')
Relations = findRelations({})
corner = findFirstCorner(Relations)
print(corner)





