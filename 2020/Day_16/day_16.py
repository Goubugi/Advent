import re

f = open('sample.txt')
text = f.read()

patternSpecifications = re.compile(': (\d+)-(\d+) or (\d+)-(\d+)')
values = re.compile('nearby tickets:((\n.*)+)')

valueNum = values.findall(text)
valueNum = list(sum(valueNum, ()))

matches = patternSpecifications.findall(text)
matches = list(sum(matches, ()))
matches = [int(x) for x in matches]
upper = [i for i in range(len(matches)) if i % 2 == 1]
lower = [i for i in range(len(matches)) if i % 2 == 0]

def isInRange(num):
    index = 0
    for fill in lower:
        l = lower[index]
        u = upper[index]
        if num < lower or num > u:
            return False
    return True

print(valueNum)




