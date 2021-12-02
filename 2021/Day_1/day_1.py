f = open('input.txt')
newList = []
data = f.readlines()
for num in data:
    if '\n' in num:
        num = num[:-1]
    num = int(num)
    newList.append(num)


def numIncreased(nL):
    index = 1
    sum = 0
    for num in nL:
        if (index < len(nL)):
            if nL[index - 1] < nL[index]:
                sum += 1
            index += 1
    return sum
print(numIncreased(newList))

sumWindows = []
index = 0
for num in newList:
    if index < len(newList)-2:
        sumWindows.append(newList[index]+newList[index+1]+newList[index+2])
    index += 1

print(numIncreased(sumWindows))


