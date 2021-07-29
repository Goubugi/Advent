f = open('sample.txt.txt')
data = f.readlines()
partOne = False

def findBuses(data):
    ret = []
    data = data.split(',')
    for i in data:
        if i != 'x':
            ret.append(int(i))
    return ret

earliest = int(data[0][:-1])
buses = findBuses(data[1])

def findEarliestBus():
    current = earliest
    while True:
        for i in buses:
            if current%i==0:
                return (current-earliest)*i
        current+=1

answer1 = findEarliestBus()
print(answer1)

