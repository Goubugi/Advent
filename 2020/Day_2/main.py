
f = open('2020/Day_2/input.txt')
newList = []
data = f.readlines()

min = []
max = []
letter = []
password = []


for i in data:
    pos = i.find('-')
    min.append(int(i[0:pos]))
    max.append(int(i[pos+1:i.find(' ')]))
    letter.append(i[i.find(' ')+1:(i.find(' ')+2)])
    password.append(i[i.find(':')+2:len(i)-1])


index = 0
listTrue = []
for i in password:
    numTimes = i.count(letter[index])
    if ((min[index]<=numTimes) & (max[index]>=numTimes)):
        listTrue.append(True)
    else:
        listTrue.append(False)
    index = index+1

print("Number Valid = ", listTrue.count(True))

index = 0
secondPart = []
min = [x -1 for x in min]
max = [x -1 for x in max]
for i in password:
    minPos = min[index]
    maxPos = max[index]
    firstPos = False
    secondPos = False
    if i[minPos] == letter[index]:
        firstPos = True
    if i[maxPos] == letter[index]:
        secondPos = True

    if (firstPos & (not secondPos)) | ((not firstPos) &  secondPos):
        secondPart.append(True)
    else:
        secondPart.append(False)

    index = index+1

print("Number Valid = ", secondPart.count(True))
