import re

f = open('input.txt')
text = f.read()

patternSpecifications = re.compile(': (\d+)-(\d+) or (\d+)-(\d+)')
values = re.compile('nearby tickets:((\n.*)+)')

valueNum = values.findall(text)
valueNum = list(sum(valueNum, ()))
valueNum = valueNum[:-1]

matches = patternSpecifications.findall(text)
matches = list(sum(matches, ()))
matches = [int(x) for x in matches]
upper = [matches[i] for i in range(len(matches)) if i % 2 == 1]
lower = [matches[i] for i in range(len(matches)) if i % 2 == 0]

temp = ""
for x in valueNum:
    temp += x
resultString = re.findall("(\d+)", temp)
finalString = []
for x in resultString:
    finalString.append(int(x))

def findAllOutOfRange():
    outOfRange = []
    for num in finalString:
        index = 0
        foundMatch = False
        for i in lower:
            lowerNum = i
            upperNum = upper[index]
            if (lowerNum <= num and num <= upperNum):
                foundMatch = True
                break
            else:
                index+=1
        if not foundMatch:
            outOfRange.append(num)
    sum = 0
    for x in outOfRange:
        sum += x
    return sum

print(findAllOutOfRange())




