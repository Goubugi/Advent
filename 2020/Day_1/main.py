

def findOutput(input):
    for i in input:
        search = 2020 - i
        if search in input:
            return(search*i)

def findOutputp2(input):
    for i in input:
        for j in input:
            newSearch = 2020-i-j
            if newSearch in input:
                return(i*newSearch*j)


input = [1721,979,366,299,675,1456]


f = open('2020/Day_1/input.txt')
newList = []
data = f.readlines()
for i in data:
    newList.append(int(i.replace('\n','')))


print(findOutputp2(newList))
