f = open('input.txt')
data = f.readlines()
partOne = True
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

if (partOne):
    recursiveSearch('shiny gold bag')
    print(f'The number of bags containing a shiny gold bag is: {len(uniqueBags)}')