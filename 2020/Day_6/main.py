f = open('input.txt')
data = f.readlines()
partOne = False
newData = []
group = []
for row in data:
    if row == '\n':
        newData.append(group)
        group = []
    elif row[-1] == '\n':
        group.append(row[:-1])
    else:
        group.append(row)
    if row == data[-1]:
        newData.append(group)

def combineString(inputList):
    returnList = []
    for group in inputList:
        returnList.append("".join(group))
    return returnList
groupSum = 0
if partOne:
    newData = combineString(newData)
    for group in newData:
        uniqueList = []
        for character in group:
            if character not in uniqueList:
                uniqueList.append(character)
        groupSum = groupSum + len(uniqueList)

    print(f'The total of sum of counts is {groupSum}')
else:
    for group in newData:
        Dict = {}
        for person in group:
            for character in person:
                if character not in Dict.keys():
                    Dict.update({character:1})
                else:
                    Dict[character] = Dict[character]+1
        allAnswerCount = 0
        for items in Dict.keys():
            if Dict[items] == len(group):
                allAnswerCount = allAnswerCount + 1
        groupSum = groupSum + allAnswerCount
    print(f'The total of sum of counts with new condition is {groupSum}')

