f = open('sample.txt')
data = f.readlines()
partOne = False
uniqueBags = []

def getDirectBags(input_bag):
    parentBags = []
    for bag in data:
        if input_bag not in bag:
            pass
        elif bag.index(input_bag) < bag.find('contain'):
            pass
        else:
            parentBags.append(bag[:bag.find('contain')-2])
    return parentBags

def getChildBags(input_bag):
    childBags = []
    childBagsNum = []
    for bag in data:
        if bag.find(input_bag)!=-1:
            if bag.index(input_bag) < bag.find('contain'):
                index = bag.find('contain')+6
                while(bag.find(',',index+1) != -1):
                    x = bag.find(',',index+1)
                    childBagsNum.append(int(bag[index + 2]))
                    childBags.append(bag[index+4:x])
                    index = bag.find(',', index+1)
                if (bag.find(' no ') == -1):
                    if bag.find(',') == -1:
                        childBags.append(bag[index+4:bag.rfind('.')])
                        childBagsNum.append(int(bag[index+2]))
                    else:
                        childBags.append(bag[bag.rfind(',')+4:bag.rfind('.')])
                        childBagsNum.append(int(bag[bag.rfind(',') + 2]))
                else:
                    childBagsNum.append(1)

    return childBags,childBagsNum


def addUnique(bagList):
    for bag in bagList:
        if bag not in uniqueBags:
            uniqueBags.append(bag)

def recursiveSearch(input_bag):
    if partOne:
        parentBags = getDirectBags(input_bag)
        addUnique(parentBags)
        for bag in parentBags:
            recursiveSearch(bag)
    else:
        childBags,childBagsNum = getChildBags(input_bag)
        total = 0
        if childBags == []:
            total = 1
        for bag in childBags:
            num = childBagsNum[childBags.index(bag)]
            recursiveNum = recursiveSearch(bag)
            if recursiveNum == 1:
                total = total + num
            else:
                total = total + recursiveNum * (num) + num
        return total

if (partOne):
    recursiveSearch('shiny gold bag')
    print(f'The number of bags containing a shiny gold bag is: {len(uniqueBags)}')


if (not partOne):
    num = recursiveSearch('shiny gold bag')
    print(f'The number of bags contained in a shiny gold bag is: {num}')



