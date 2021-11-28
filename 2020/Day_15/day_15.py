data = [9,12,1,4,17,0,18]
mapLastCalled = {}
last = data[0]
total = 30000000

for x in range(0, len(data)):
    mapLastCalled.update({data[x]:[x+1, -1]})
    last = data[x]

current = 0
def update(first, second):
    if (first in mapLastCalled) :
        if (mapLastCalled.get(first)[1] == -1):
            mapLastCalled.update({first: [mapLastCalled.get(first)[0], second]})
        else:
            mapLastCalled.update({first: [mapLastCalled.get(first)[1], second]})
    else:
        mapLastCalled.update({first: [second, -1]})


for x in range(len(data)+1, total+1):
    if (last in mapLastCalled and mapLastCalled.get(last)[1] != -1):
        current = mapLastCalled.get(last)[1] - mapLastCalled.get(last)[0]
        update(current, x)
        last = current
    else:
        update(0, x)
        last = 0


