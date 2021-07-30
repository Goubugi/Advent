f = open('input.txt')
data = f.readlines()
partOne = False

def findBuses(data):
    ret = []
    data = data.split(',')
    for i in data:
        if i != 'x':
            ret.append(int(i))
    return ret

def findBuses2(data):
    ret = []
    data = data.split(',')
    for i in data:
        if i != 'x':
            ret.append(int(i))
        else:
            ret.append(i)
    return ret

earliest = int(data[0][:-1])
buses = findBuses(data[1])

buses2 = findBuses2(data[1])

def findEarliestBus():
    current = earliest
    while True:
        for i in buses:
            if current%i==0:
                return (current-earliest)*i
        current+=1

def findEarliestPattern():
    count = 0
    skip = buses[0]
    added = [buses[0]]
    while True:
        index = 0
        for i in buses2:
            if i == 'x':
                pass
            else:
                if (count+index)%i==0:
                    if i not in added:
                        added.append(i)
                        skip *= i
                    if i == buses2[-1]:
                        return count
                else:
                    break
            index+=1
        count+=skip



if partOne:
    answer1 = findEarliestBus()
    print(answer1)
else:
    answer2 = findEarliestPattern()
    print(answer2)

