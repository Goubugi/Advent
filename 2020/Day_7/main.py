f = open('input.txt')
data = f.readlines()

def recursionPartTwo(newData, input_bag):
    count = 0
    list = newData[input_bag]
    if list == []:
        return count
    for bagType in list:
        count += bagType['count']
        recursiveValue = recursionPartTwo(newData, bagType['type'])
        count += bagType['count'] * recursiveValue

    return count

def parseNewData():
    newData = {}
    for bag in data:
        tempList = []
        index = bag.find('contain')+7
        color = (bag[:index-13])
        while bag.find(',',index)!= -1:
            count = int(bag[index+1])
            if (count == 1):
                newColor = bag[index+3:bag.find(',',index)-4]
            else:
                newColor = bag[index + 3:bag.find(',', index)-5]
            index = bag.find(',',index)+1
            tempList.append({'count':count,'type':newColor})
        if bag.find(' no ') != -1:
            newData.update({color:[]})
        elif bag.find(',') == -1:
            count = int(bag[index+1])
            if count == 1:
                newColor = bag[index+3:bag.rfind('.')-4]
            else:
                newColor = bag[index + 3:bag.rfind('.')-5]
            tempList.append({'count':count,'type':newColor})
            newData.update({color:tempList})
        else:
            index = bag.rfind(',')
            count = int(bag[index+2])
            if count == 1:
                newColor = bag[index+4:bag.find('.',index)-4]
            else:
                newColor = bag[index + 4:bag.find('.', index)-5]
            tempList.append({'count':count,'type':newColor})
            newData.update({color:tempList})

    return newData

import re

main_raw_input = """shiny indigo bags contain 4 vibrant lime bags.
clear lime bags contain 1 dotted lime bag, 2 clear gold bags.
dotted turquoise bags contain 2 shiny green bags, 5 striped magenta bags, 3 muted green bags.
bright red bags contain 1 plaid magenta bag, 3 light cyan bags.
vibrant magenta bags contain 5 drab lime bags, 3 muted red bags, 3 wavy turquoise bags, 3 mirrored salmon bags.
plaid violet bags contain 4 plaid indigo bags, 1 mirrored beige bag.
muted gray bags contain 2 striped crimson bags, 2 striped maroon bags, 1 faded maroon bag, 4 dim lavender bags.
mirrored crimson bags contain 5 muted lavender bags.
muted gold bags contain 3 striped plum bags, 4 bright coral bags.
pale black bags contain 4 shiny orange bags, 3 pale bronze bags, 2 wavy coral bags.
muted purple bags contain 5 muted brown bags.
clear cyan bags contain 4 muted white bags.
shiny blue bags contain 5 pale magenta bags, 3 drab coral bags.
posh white bags contain 3 posh brown bags, 3 striped gold bags, 1 faded gray bag.
muted beige bags contain 1 pale teal bag.
clear purple bags contain 4 plaid turquoise bags.
pale gold bags contain 1 mirrored lime bag, 2 dim crimson bags, 3 dim aqua bags, 2 dull silver bags.
pale beige bags contain 4 drab olive bags, 2 wavy coral bags.
drab black bags contain 4 mirrored blue bags, 2 light olive bags.
faded purple bags contain 3 dim lime bags, 2 vibrant violet bags.
pale silver bags contain 3 light cyan bags.
plaid teal bags contain 3 dotted fuchsia bags, 3 bright teal bags.
plaid beige bags contain 5 shiny black bags, 3 dotted maroon bags.
light silver bags contain 3 posh chartreuse bags, 4 dark bronze bags, 1 vibrant silver bag, 2 muted coral bags.
pale plum bags contain 5 drab silver bags, 4 light crimson bags.
striped cyan bags contain 3 wavy tan bags, 5 pale teal bags, 5 clear orange bags, 3 wavy violet bags.
plaid red bags contain 2 dim lavender bags, 4 striped maroon bags.
dark salmon bags contain 5 bright gold bags, 5 muted lavender bags, 5 light beige bags.
shiny purple bags contain 2 plaid silver bags, 2 mirrored green bags, 3 bright violet bags.
shiny turquoise bags contain 1 vibrant salmon bag.
muted orange bags contain 2 striped indigo bags, 1 striped crimson bag.
pale turquoise bags contain 3 light silver bags, 5 light crimson bags.
light indigo bags contain 4 vibrant white bags, 5 plaid yellow bags.
faded coral bags contain 1 vibrant beige bag, 4 muted white bags.
dim red bags contain 1 mirrored cyan bag, 2 wavy indigo bags, 5 shiny chartreuse bags, 5 muted yellow bags.
striped fuchsia bags contain 2 faded salmon bags, 1 pale beige bag, 2 posh magenta bags, 2 wavy green bags.
bright green bags contain 4 pale turquoise bags, 2 bright chartreuse bags, 5 posh yellow bags, 4 shiny gold bags.
light blue bags contain 5 dim silver bags.
vibrant purple bags contain 3 wavy indigo bags, 1 pale maroon bag, 3 drab chartreuse bags, 5 vibrant aqua bags.
light coral bags contain 2 clear orange bags, 3 shiny fuchsia bags, 3 striped chartreuse bags.
striped maroon bags contain 4 vibrant tomato bags, 2 dull salmon bags, 1 shiny gold bag, 2 muted coral bags.
drab lime bags contain 1 mirrored violet bag, 4 posh magenta bags.
dotted gold bags contain 3 muted silver bags.
pale magenta bags contain 5 mirrored orange bags, 4 pale teal bags.
dim olive bags contain no other bags.
mirrored blue bags contain 1 dim indigo bag, 4 bright lime bags, 1 plaid beige bag.
plaid bronze bags contain 3 pale gold bags.
faded aqua bags contain 3 muted aqua bags, 3 muted gray bags, 4 dim olive bags.
light gold bags contain 1 mirrored crimson bag, 3 pale tan bags, 3 dotted yellow bags, 2 wavy aqua bags.
dim gold bags contain 4 plaid tomato bags.
faded chartreuse bags contain 5 muted coral bags, 4 vibrant indigo bags, 1 faded teal bag, 1 vibrant bronze bag.
posh brown bags contain 2 muted gray bags, 1 dark plum bag, 3 bright lime bags, 2 dull turquoise bags.
mirrored lime bags contain 1 shiny indigo bag, 4 dark olive bags, 3 pale beige bags.
posh cyan bags contain 3 pale olive bags.
dark lime bags contain 3 shiny cyan bags, 4 bright green bags.
drab lavender bags contain 4 drab plum bags.
vibrant orange bags contain 5 wavy olive bags.
faded violet bags contain 1 faded aqua bag, 2 muted gray bags.
light green bags contain 5 pale brown bags, 4 dark aqua bags, 5 vibrant teal bags, 1 pale black bag.
bright turquoise bags contain 4 striped teal bags, 2 dim magenta bags, 5 striped orange bags, 4 bright aqua bags.
mirrored indigo bags contain 2 wavy violet bags, 2 muted white bags, 2 dim lavender bags.
wavy green bags contain 5 dotted teal bags.
light aqua bags contain 4 posh lime bags, 1 dotted maroon bag, 3 dotted gray bags, 2 plaid bronze bags.
muted tomato bags contain 3 mirrored tomato bags, 3 pale blue bags, 2 mirrored violet bags, 4 drab tomato bags.
posh beige bags contain 5 faded aqua bags.
shiny coral bags contain 5 striped gold bags, 1 drab coral bag, 2 light lavender bags, 4 striped blue bags.
posh orange bags contain 5 dark olive bags, 3 light silver bags, 3 striped gray bags, 2 faded fuchsia bags.
posh violet bags contain 2 drab turquoise bags, 5 mirrored gray bags.
pale brown bags contain 2 bright chartreuse bags.
shiny green bags contain 2 mirrored magenta bags.
faded salmon bags contain 2 wavy tan bags.
dark gold bags contain no other bags.
clear black bags contain 5 vibrant lime bags.
muted fuchsia bags contain 1 pale fuchsia bag, 4 mirrored white bags, 3 clear fuchsia bags, 3 faded maroon bags.
drab fuchsia bags contain 1 bright chartreuse bag, 3 pale beige bags, 5 wavy brown bags.
mirrored plum bags contain 1 plaid yellow bag, 2 dim beige bags, 5 dim aqua bags, 4 dim crimson bags.
dark maroon bags contain 1 striped crimson bag, 5 muted fuchsia bags, 3 vibrant silver bags, 2 drab olive bags.
drab green bags contain 5 faded bronze bags, 2 bright violet bags, 3 dark gold bags.
drab purple bags contain 3 plaid orange bags, 4 striped black bags, 5 vibrant indigo bags, 4 pale turquoise bags.
dotted silver bags contain 1 clear crimson bag, 2 faded yellow bags.
dull olive bags contain 3 muted salmon bags, 2 vibrant cyan bags, 3 posh bronze bags, 5 light cyan bags.
posh gold bags contain 4 bright violet bags, 1 drab yellow bag.
dark plum bags contain 4 clear fuchsia bags, 2 mirrored aqua bags.
dim purple bags contain 5 clear chartreuse bags, 4 dark gold bags.
drab tomato bags contain 5 mirrored white bags.
mirrored chartreuse bags contain 3 clear indigo bags, 4 clear crimson bags.
striped olive bags contain 4 posh orange bags, 5 shiny indigo bags.
dark purple bags contain 2 drab lavender bags, 2 faded bronze bags.
light purple bags contain 1 vibrant lime bag, 2 vibrant gray bags.
mirrored green bags contain 4 mirrored cyan bags.
bright lavender bags contain 1 dark red bag, 2 clear yellow bags, 3 bright brown bags, 2 bright teal bags.
posh tomato bags contain 4 posh silver bags, 3 shiny black bags, 4 clear crimson bags, 3 dotted chartreuse bags.
dotted coral bags contain 4 dotted bronze bags, 5 dotted maroon bags.
pale cyan bags contain 2 dim coral bags, 4 dotted brown bags.
plaid gold bags contain 4 bright chartreuse bags, 4 faded bronze bags.
bright tan bags contain 3 bright brown bags.
dim chartreuse bags contain 2 clear maroon bags, 3 pale tan bags, 2 mirrored lime bags, 1 wavy crimson bag.
dark bronze bags contain 4 faded maroon bags, 1 wavy violet bag, 4 plaid silver bags.
wavy brown bags contain 4 light red bags, 2 dull tomato bags, 5 mirrored red bags, 4 bright lime bags.
dim fuchsia bags contain 4 dark beige bags.
drab bronze bags contain 2 dotted blue bags.
bright plum bags contain 2 plaid orange bags.
shiny red bags contain 1 faded fuchsia bag.
vibrant brown bags contain 3 faded fuchsia bags, 2 light plum bags.
pale tan bags contain 3 dark aqua bags, 3 dark plum bags, 1 mirrored green bag.
dull aqua bags contain 3 muted cyan bags, 5 drab cyan bags.
dark teal bags contain 1 light red bag, 4 plaid silver bags, 2 dark olive bags, 5 striped maroon bags.
pale tomato bags contain 4 dim indigo bags, 4 dark salmon bags.
faded silver bags contain 5 dim blue bags.
striped lime bags contain 2 bright black bags.
plaid coral bags contain 4 dull salmon bags, 5 mirrored green bags, 1 pale aqua bag.
clear white bags contain 4 drab turquoise bags, 2 posh coral bags, 5 dark fuchsia bags.
dark turquoise bags contain 1 wavy lavender bag, 4 bright lime bags.
dark tomato bags contain 5 faded maroon bags, 4 dark chartreuse bags, 5 wavy fuchsia bags, 2 dotted purple bags.
striped bronze bags contain no other bags.
dark black bags contain 2 dotted chartreuse bags, 3 pale bronze bags.
dotted teal bags contain 2 dark teal bags.
drab yellow bags contain 3 dark turquoise bags, 4 muted fuchsia bags.
wavy salmon bags contain 2 plaid turquoise bags.
dull violet bags contain 3 mirrored red bags, 5 shiny black bags, 3 dark maroon bags.
muted cyan bags contain 4 mirrored black bags, 4 dim olive bags, 1 bright chartreuse bag, 1 clear bronze bag.
clear plum bags contain 4 light teal bags, 1 faded white bag, 3 striped lime bags.
light red bags contain 3 mirrored orange bags.
pale gray bags contain 5 wavy cyan bags, 2 bright green bags, 3 striped gray bags.
posh green bags contain 3 clear purple bags.
dark crimson bags contain 5 bright violet bags, 4 light magenta bags, 1 posh chartreuse bag, 1 shiny gray bag.
dull yellow bags contain 1 dotted fuchsia bag, 5 muted maroon bags, 1 muted salmon bag.
plaid plum bags contain 1 striped olive bag.
wavy lime bags contain 3 vibrant silver bags, 5 shiny gold bags.
dim green bags contain 1 dark tomato bag, 5 light red bags, 4 muted gold bags.
mirrored yellow bags contain 1 vibrant tomato bag.
dotted yellow bags contain 3 striped crimson bags.
drab turquoise bags contain 1 clear indigo bag, 1 mirrored magenta bag, 4 clear violet bags.
dim aqua bags contain 3 wavy coral bags, 1 posh beige bag.
pale violet bags contain 1 faded plum bag, 4 dull purple bags, 2 pale brown bags.
muted crimson bags contain 3 dim beige bags, 2 dim gray bags.
mirrored brown bags contain 1 dotted tan bag, 4 dim olive bags, 1 bright lime bag.
dotted crimson bags contain 5 striped beige bags, 4 striped turquoise bags, 3 shiny fuchsia bags.
mirrored tan bags contain 5 bright indigo bags, 3 light violet bags.
striped black bags contain 4 striped olive bags.
faded fuchsia bags contain 3 faded teal bags, 4 dull salmon bags, 3 light red bags.
dull green bags contain 4 mirrored coral bags.
vibrant blue bags contain 1 striped gray bag, 4 striped olive bags, 3 wavy brown bags, 3 faded maroon bags.
vibrant plum bags contain 4 wavy brown bags, 5 clear violet bags, 3 pale turquoise bags, 2 posh crimson bags.
wavy fuchsia bags contain 5 wavy olive bags.
striped red bags contain 2 pale yellow bags, 3 pale chartreuse bags, 1 dim blue bag.
muted blue bags contain 2 posh red bags, 2 muted red bags, 3 dark tomato bags.
muted plum bags contain 4 plaid red bags.
clear violet bags contain 5 muted salmon bags.
pale white bags contain 3 plaid lavender bags, 5 mirrored green bags.
clear beige bags contain 2 vibrant blue bags, 5 muted white bags, 2 dull chartreuse bags.
vibrant fuchsia bags contain 4 posh gray bags, 5 dull tomato bags, 3 dim crimson bags.
dim indigo bags contain 1 bright black bag, 5 faded black bags, 5 dull turquoise bags, 2 mirrored lime bags.
dotted lime bags contain 3 light lime bags, 4 pale salmon bags, 4 dark aqua bags.
posh teal bags contain 3 pale gold bags, 2 faded silver bags.
faded gray bags contain 2 shiny gold bags, 1 dull turquoise bag, 1 faded chartreuse bag.
dim magenta bags contain 2 mirrored aqua bags, 5 wavy orange bags, 3 pale turquoise bags.
shiny fuchsia bags contain 5 vibrant silver bags.
drab teal bags contain 3 posh magenta bags, 2 striped indigo bags, 5 muted salmon bags, 4 shiny plum bags.
bright indigo bags contain 2 faded teal bags.
muted teal bags contain 4 mirrored green bags, 3 dull violet bags, 3 shiny purple bags.
light tan bags contain 1 muted salmon bag, 1 plaid olive bag, 2 plaid silver bags.
striped yellow bags contain 2 drab salmon bags, 2 faded aqua bags.
mirrored olive bags contain 5 clear maroon bags, 2 striped coral bags, 4 dim gold bags.
wavy cyan bags contain 3 plaid lavender bags, 1 wavy turquoise bag, 2 plaid bronze bags, 1 light beige bag.
mirrored red bags contain no other bags.
light yellow bags contain 3 dim purple bags, 4 posh green bags, 3 pale gold bags.
dotted gray bags contain 3 dotted orange bags, 5 plaid turquoise bags, 4 drab magenta bags.
faded red bags contain 3 bright aqua bags.
dull teal bags contain 4 clear purple bags, 5 faded turquoise bags.
light salmon bags contain 3 posh lime bags, 1 clear lime bag, 1 drab chartreuse bag, 3 clear magenta bags.
dark red bags contain 1 plaid tomato bag, 1 plaid orange bag, 4 dotted white bags.
mirrored beige bags contain 3 mirrored violet bags, 3 clear orange bags, 3 dark olive bags.
drab indigo bags contain 2 muted aqua bags, 3 bright teal bags.
light lime bags contain 4 light indigo bags, 5 plaid white bags.
pale blue bags contain 3 wavy tan bags, 1 mirrored tomato bag, 5 faded magenta bags, 2 posh crimson bags.
drab plum bags contain 2 striped crimson bags.
striped tomato bags contain 1 dark maroon bag.
faded maroon bags contain 3 drab salmon bags, 5 posh lime bags, 4 dim olive bags, 5 striped bronze bags.
clear fuchsia bags contain 5 vibrant silver bags, 5 posh lime bags, 4 striped crimson bags.
bright maroon bags contain 2 dull gray bags, 4 bright magenta bags, 5 clear beige bags, 5 vibrant silver bags.
clear blue bags contain 4 faded black bags, 2 plaid magenta bags, 1 clear salmon bag, 1 shiny chartreuse bag.
plaid chartreuse bags contain 1 dark bronze bag, 1 clear red bag, 2 mirrored plum bags, 4 posh white bags.
pale crimson bags contain 4 muted silver bags.
clear olive bags contain 3 dark olive bags, 5 drab plum bags, 2 striped maroon bags, 5 shiny purple bags.
vibrant indigo bags contain 1 vibrant silver bag, 5 dark olive bags, 1 striped chartreuse bag, 1 muted fuchsia bag.
dim coral bags contain 2 dark yellow bags, 3 clear orange bags, 2 clear cyan bags, 1 pale turquoise bag.
shiny white bags contain 3 drab teal bags, 3 vibrant blue bags.
vibrant tan bags contain 3 posh red bags, 1 faded black bag, 3 faded aqua bags, 2 light beige bags.
wavy plum bags contain 1 dotted teal bag, 3 dark indigo bags.
drab coral bags contain 3 clear orange bags, 4 shiny red bags, 5 bright teal bags.
mirrored aqua bags contain 3 mirrored cyan bags, 5 wavy coral bags.
vibrant gray bags contain 2 muted coral bags, 1 clear fuchsia bag.
faded turquoise bags contain 2 posh lime bags.
clear green bags contain 4 posh yellow bags, 3 light bronze bags, 4 drab gray bags, 3 bright teal bags.
wavy gold bags contain 3 faded black bags, 4 faded violet bags.
shiny tan bags contain 4 mirrored gray bags, 3 mirrored magenta bags, 5 light red bags.
plaid turquoise bags contain 5 faded aqua bags, 3 mirrored tomato bags, 5 light tan bags, 2 drab olive bags.
pale bronze bags contain 5 drab chartreuse bags, 4 faded lime bags.
mirrored lavender bags contain 3 plaid green bags, 1 clear salmon bag, 3 dim gray bags.
pale yellow bags contain 3 drab yellow bags, 5 drab green bags, 1 drab lavender bag, 1 clear magenta bag.
mirrored teal bags contain 5 posh black bags.
vibrant teal bags contain 1 dark teal bag.
bright gold bags contain 3 dark green bags, 4 clear orange bags, 1 shiny purple bag, 5 dull chartreuse bags.
muted lavender bags contain 5 faded fuchsia bags.
light gray bags contain 5 plaid magenta bags, 3 vibrant cyan bags, 3 bright gold bags, 2 dim cyan bags.
dark gray bags contain 3 posh silver bags, 1 dark fuchsia bag, 5 dark teal bags, 5 clear fuchsia bags.
mirrored gold bags contain 5 dim crimson bags, 2 plaid beige bags, 3 dark coral bags.
wavy violet bags contain 5 dull silver bags, 3 dark gold bags, 5 striped bronze bags.
vibrant cyan bags contain 2 bright indigo bags.
dull tan bags contain 2 shiny indigo bags, 2 dim gold bags, 5 vibrant blue bags, 4 dull tomato bags.
dim orange bags contain 5 posh silver bags, 3 light red bags.
drab gold bags contain 4 shiny indigo bags, 2 clear indigo bags, 1 faded fuchsia bag, 1 muted crimson bag.
vibrant bronze bags contain 3 mirrored green bags, 2 striped gold bags, 5 wavy coral bags.
light violet bags contain 3 dull turquoise bags, 5 light white bags, 2 drab coral bags.
plaid tomato bags contain 1 wavy tan bag, 2 faded maroon bags.
faded black bags contain 4 dark bronze bags.
drab violet bags contain 2 pale green bags, 5 muted olive bags.
dull lavender bags contain 5 light chartreuse bags, 5 striped fuchsia bags, 2 clear white bags, 5 dull indigo bags.
light chartreuse bags contain 5 dim lavender bags.
dim salmon bags contain 5 shiny silver bags, 4 dark coral bags, 2 vibrant cyan bags, 3 faded black bags.
posh blue bags contain 4 clear bronze bags, 5 shiny aqua bags, 1 vibrant brown bag.
light crimson bags contain 4 plaid aqua bags, 3 mirrored green bags.
striped plum bags contain 5 plaid white bags, 5 light beige bags.
shiny bronze bags contain 5 dark magenta bags.
dark fuchsia bags contain 5 posh crimson bags, 3 dark turquoise bags, 1 vibrant white bag.
striped coral bags contain 5 dim gray bags.
vibrant gold bags contain 5 dull tomato bags, 3 mirrored cyan bags, 2 light tan bags.
wavy tan bags contain 2 faded maroon bags, 4 wavy violet bags.
dotted violet bags contain 5 shiny blue bags.
faded bronze bags contain 3 shiny gold bags.
plaid tan bags contain 3 posh tan bags, 5 mirrored cyan bags, 1 drab lavender bag, 4 shiny blue bags.
plaid salmon bags contain 2 faded coral bags.
dark orange bags contain 3 light purple bags, 5 wavy blue bags, 2 muted crimson bags, 2 dull magenta bags.
wavy beige bags contain 1 muted silver bag, 5 bright yellow bags.
plaid cyan bags contain 4 dark orange bags, 5 dark plum bags, 5 dotted tomato bags, 5 striped magenta bags.
dark lavender bags contain 2 mirrored beige bags, 1 pale blue bag, 2 dull chartreuse bags, 5 mirrored black bags.
light black bags contain 1 dull tomato bag, 5 bright violet bags.
wavy silver bags contain 2 clear gold bags.
wavy maroon bags contain 2 posh tomato bags, 5 shiny maroon bags, 1 wavy yellow bag.
clear lavender bags contain 1 muted white bag, 5 striped chartreuse bags, 3 dark salmon bags, 1 plaid teal bag.
dotted brown bags contain 4 striped blue bags, 3 mirrored fuchsia bags, 3 posh red bags.
faded teal bags contain 4 plaid olive bags.
clear gray bags contain 2 mirrored fuchsia bags, 4 faded blue bags.
light tomato bags contain 5 wavy indigo bags, 2 posh beige bags.
muted black bags contain 1 dark lime bag, 1 striped green bag.
dotted beige bags contain 5 faded lavender bags, 3 plaid yellow bags.
posh turquoise bags contain 1 wavy indigo bag.
bright crimson bags contain 1 dark fuchsia bag.
striped teal bags contain 3 vibrant olive bags, 1 bright maroon bag, 3 muted teal bags, 4 clear yellow bags.
clear orange bags contain 3 shiny plum bags, 3 drab olive bags.
posh silver bags contain 5 mirrored violet bags, 2 dotted teal bags.
dim gray bags contain 4 pale teal bags, 5 muted salmon bags, 3 dark indigo bags.
dotted tomato bags contain 3 dotted maroon bags.
posh purple bags contain 3 drab turquoise bags, 3 dark olive bags, 4 posh lime bags, 1 posh orange bag.
vibrant beige bags contain 2 mirrored violet bags, 1 mirrored white bag, 1 wavy violet bag.
dark tan bags contain 5 bright violet bags, 5 light blue bags, 4 shiny plum bags, 1 light indigo bag.
dim lavender bags contain 3 mirrored green bags, 1 wavy tan bag, 2 striped crimson bags, 5 wavy violet bags.
faded crimson bags contain 3 muted yellow bags, 2 posh lime bags, 5 mirrored gray bags, 3 faded chartreuse bags.
posh coral bags contain 3 muted silver bags, 4 pale magenta bags, 1 light orange bag.
dull tomato bags contain 2 plaid tomato bags, 2 dim lavender bags, 4 mirrored orange bags, 3 clear fuchsia bags.
striped orange bags contain 2 vibrant teal bags, 1 dotted teal bag.
shiny maroon bags contain 5 light beige bags, 1 dim lime bag.
pale olive bags contain 2 mirrored gold bags, 4 plaid tomato bags.
light olive bags contain 1 light red bag, 1 light crimson bag, 2 striped chartreuse bags.
posh plum bags contain 5 bright silver bags, 4 vibrant indigo bags, 4 pale turquoise bags.
shiny orange bags contain 4 dim chartreuse bags, 2 dotted lavender bags, 2 shiny green bags.
pale indigo bags contain 3 mirrored chartreuse bags, 5 mirrored violet bags, 2 vibrant blue bags, 3 mirrored maroon bags.
posh tan bags contain 5 shiny plum bags, 2 dark aqua bags.
bright blue bags contain 5 vibrant salmon bags, 5 bright maroon bags, 1 muted yellow bag.
clear maroon bags contain 4 vibrant beige bags, 3 mirrored gold bags, 2 drab teal bags, 2 drab plum bags.
wavy chartreuse bags contain 3 clear olive bags, 1 drab lavender bag.
drab gray bags contain 5 plaid salmon bags.
faded orange bags contain 1 faded maroon bag, 5 vibrant orange bags.
bright coral bags contain 3 pale turquoise bags.
light beige bags contain 1 muted cyan bag.
plaid maroon bags contain 5 faded magenta bags, 4 faded bronze bags.
dotted purple bags contain 1 drab plum bag, 5 faded black bags, 2 dull silver bags.
muted salmon bags contain no other bags.
striped blue bags contain 5 mirrored lime bags, 2 dark plum bags.
dotted lavender bags contain 2 faded salmon bags, 3 dim silver bags, 1 clear cyan bag, 4 plaid lavender bags.
wavy black bags contain 4 vibrant gold bags, 5 light black bags, 4 muted aqua bags, 5 vibrant white bags.
clear aqua bags contain 3 plaid beige bags, 1 plaid white bag, 3 shiny red bags, 3 wavy crimson bags.
mirrored cyan bags contain no other bags.
shiny brown bags contain 2 dim aqua bags.
dotted green bags contain 4 mirrored green bags, 3 mirrored tomato bags, 5 plaid gray bags.
striped purple bags contain 3 wavy yellow bags, 2 faded orange bags.
plaid indigo bags contain 2 shiny plum bags, 5 bright magenta bags, 2 posh yellow bags, 3 shiny gold bags.
posh chartreuse bags contain 2 mirrored cyan bags, 4 drab salmon bags, 4 dim olive bags, 2 posh lime bags.
light lavender bags contain 4 dim fuchsia bags, 5 pale salmon bags, 4 clear teal bags.
shiny crimson bags contain 5 light blue bags.
plaid black bags contain 5 clear indigo bags, 5 mirrored purple bags, 1 light aqua bag.
shiny lime bags contain 5 dotted blue bags, 2 shiny tan bags.
dotted salmon bags contain 4 pale salmon bags, 1 clear maroon bag.
vibrant lavender bags contain 4 shiny red bags, 4 shiny green bags, 5 dim silver bags.
muted yellow bags contain 5 wavy aqua bags, 2 posh lavender bags, 3 dull magenta bags, 1 plaid red bag.
faded beige bags contain 1 wavy violet bag, 4 plaid maroon bags.
wavy blue bags contain 5 dotted orange bags, 1 faded chartreuse bag, 4 posh magenta bags.
faded brown bags contain 4 bright coral bags, 3 mirrored aqua bags.
striped lavender bags contain 5 dim brown bags, 2 wavy cyan bags, 4 pale blue bags, 1 posh olive bag.
bright fuchsia bags contain 5 clear lime bags.
bright black bags contain 5 clear fuchsia bags, 4 pale purple bags.
pale orange bags contain 3 plaid aqua bags, 5 muted fuchsia bags, 1 wavy crimson bag.
mirrored magenta bags contain 2 posh chartreuse bags, 2 muted white bags, 5 posh lime bags, 5 dark gold bags.
light magenta bags contain 1 mirrored white bag, 1 dull silver bag, 5 posh chartreuse bags.
striped gold bags contain 1 mirrored cyan bag, 1 dark olive bag, 4 mirrored red bags, 5 posh chartreuse bags.
plaid lavender bags contain 1 vibrant white bag, 4 dotted maroon bags.
faded gold bags contain 5 striped crimson bags.
vibrant olive bags contain 1 plaid beige bag.
dark aqua bags contain 4 plaid tomato bags, 1 striped olive bag, 4 pale fuchsia bags, 3 dim gold bags.
dim lime bags contain 2 plaid gray bags.
pale lavender bags contain 4 muted yellow bags, 1 drab yellow bag, 2 dull cyan bags, 2 muted teal bags.
bright violet bags contain 2 posh lime bags, 1 wavy violet bag, 2 mirrored red bags.
dotted maroon bags contain 1 drab salmon bag.
clear magenta bags contain 3 mirrored brown bags.
vibrant red bags contain 5 clear cyan bags, 2 dark teal bags.
shiny olive bags contain 5 light tan bags, 5 plaid maroon bags, 3 mirrored blue bags.
plaid fuchsia bags contain 5 posh silver bags.
vibrant chartreuse bags contain 2 clear coral bags, 2 pale purple bags, 5 light beige bags.
vibrant violet bags contain 3 striped bronze bags, 2 drab tomato bags, 2 faded violet bags, 5 posh crimson bags.
vibrant white bags contain 1 plaid orange bag, 5 muted aqua bags, 5 pale fuchsia bags, 3 muted fuchsia bags.
drab magenta bags contain 3 bright indigo bags, 1 faded violet bag.
faded tan bags contain 3 dark crimson bags, 5 light aqua bags.
bright salmon bags contain 3 clear plum bags, 3 striped blue bags, 5 plaid green bags.
wavy aqua bags contain 1 clear beige bag, 5 dull magenta bags.
muted white bags contain 5 wavy tan bags, 5 plaid silver bags, 5 striped bronze bags, 3 dull silver bags.
mirrored gray bags contain 4 dim olive bags, 3 striped gold bags, 1 wavy tan bag, 5 striped bronze bags.
vibrant maroon bags contain 5 clear bronze bags.
shiny violet bags contain 2 clear salmon bags, 1 bright beige bag.
dim bronze bags contain 2 posh brown bags, 4 vibrant indigo bags, 2 dull purple bags.
bright bronze bags contain 1 bright maroon bag, 4 faded aqua bags, 2 pale tan bags, 3 mirrored lavender bags.
dull blue bags contain 4 clear coral bags, 2 drab olive bags.
posh crimson bags contain 1 muted white bag, 2 faded maroon bags, 5 plaid olive bags.
dark olive bags contain 3 dim olive bags, 3 mirrored red bags.
striped violet bags contain 4 wavy gold bags, 4 dotted maroon bags, 1 vibrant salmon bag.
vibrant tomato bags contain 1 striped gold bag, 1 faded turquoise bag.
mirrored turquoise bags contain 2 dark magenta bags, 2 clear lime bags, 3 dull turquoise bags.
mirrored coral bags contain 4 plaid lavender bags, 4 vibrant salmon bags, 4 mirrored chartreuse bags, 3 plaid white bags.
muted red bags contain 2 mirrored maroon bags, 4 vibrant beige bags.
shiny salmon bags contain 2 posh black bags, 4 wavy tan bags.
vibrant turquoise bags contain 4 clear crimson bags.
pale maroon bags contain 4 striped crimson bags, 5 wavy indigo bags, 3 dull turquoise bags, 2 faded black bags.
dull beige bags contain 4 dim olive bags, 3 vibrant olive bags, 1 mirrored plum bag, 3 muted white bags.
striped tan bags contain 5 mirrored gray bags.
dotted magenta bags contain 4 wavy olive bags, 5 mirrored magenta bags, 4 muted fuchsia bags, 2 muted gray bags.
pale chartreuse bags contain 1 wavy crimson bag.
dull white bags contain 1 dull tomato bag, 4 faded tomato bags, 3 shiny fuchsia bags, 4 dim beige bags.
light cyan bags contain 3 drab plum bags, 1 wavy violet bag, 1 vibrant gold bag, 1 dotted purple bag.
bright tomato bags contain 1 bright plum bag.
bright olive bags contain 1 dull green bag.
shiny tomato bags contain 3 faded red bags, 3 mirrored gold bags.
light white bags contain 2 dotted gray bags.
dotted bronze bags contain 3 wavy olive bags.
drab white bags contain 4 dim fuchsia bags.
posh indigo bags contain 2 dull salmon bags, 4 mirrored white bags.
vibrant coral bags contain 2 faded chartreuse bags, 3 dark indigo bags, 1 wavy coral bag.
bright purple bags contain 4 dull white bags.
faded blue bags contain 1 striped chartreuse bag, 2 faded crimson bags.
striped turquoise bags contain 5 dark plum bags.
faded green bags contain 1 mirrored white bag, 1 striped magenta bag.
dotted indigo bags contain 5 pale olive bags, 5 vibrant fuchsia bags.
drab blue bags contain 2 faded tomato bags.
dull lime bags contain 4 faded crimson bags, 1 striped white bag, 3 drab bronze bags.
bright yellow bags contain 5 drab purple bags, 2 mirrored white bags, 4 faded fuchsia bags, 2 dark tomato bags.
clear turquoise bags contain 3 muted fuchsia bags, 3 plaid purple bags, 4 posh blue bags.
dull crimson bags contain 5 muted green bags, 3 dotted bronze bags, 2 pale gray bags.
light maroon bags contain 5 faded indigo bags, 1 clear yellow bag.
wavy magenta bags contain 3 bright orange bags, 2 pale lavender bags, 1 shiny blue bag, 1 plaid purple bag.
vibrant aqua bags contain 2 vibrant silver bags.
posh black bags contain 3 striped crimson bags.
bright white bags contain 2 clear white bags.
clear bronze bags contain 2 dim aqua bags, 1 mirrored indigo bag.
vibrant yellow bags contain 2 vibrant silver bags.
bright silver bags contain 3 clear beige bags, 3 mirrored lime bags.
plaid magenta bags contain 5 striped gold bags, 5 posh purple bags, 2 pale brown bags.
shiny black bags contain 2 posh beige bags, 4 posh magenta bags, 4 dim blue bags, 4 dark bronze bags.
shiny yellow bags contain 2 wavy turquoise bags, 2 pale purple bags.
plaid aqua bags contain 3 shiny fuchsia bags, 1 dull tomato bag, 2 light magenta bags, 3 mirrored green bags.
wavy bronze bags contain 2 bright gold bags, 5 plaid green bags, 1 shiny violet bag, 1 faded chartreuse bag.
mirrored purple bags contain 2 faded tomato bags, 1 dark gold bag, 4 dim aqua bags, 1 faded aqua bag.
muted tan bags contain 3 pale teal bags, 3 drab tomato bags, 4 pale maroon bags, 1 dim cyan bag.
plaid blue bags contain 2 muted coral bags, 5 striped maroon bags, 3 pale plum bags, 5 dotted purple bags.
posh gray bags contain 5 muted salmon bags, 2 wavy orange bags.
wavy orange bags contain 5 dark aqua bags.
bright brown bags contain 3 muted yellow bags, 5 faded lavender bags, 2 drab cyan bags, 2 mirrored indigo bags.
dark brown bags contain 3 plaid coral bags.
bright beige bags contain 4 vibrant indigo bags, 5 bright lime bags, 5 bright magenta bags.
clear tan bags contain 3 dark turquoise bags, 4 vibrant cyan bags.
light brown bags contain 3 light lime bags.
wavy red bags contain 5 wavy cyan bags, 4 plaid bronze bags, 3 dark chartreuse bags.
faded olive bags contain 1 wavy green bag, 3 drab olive bags.
vibrant lime bags contain 5 vibrant silver bags, 2 light silver bags.
faded plum bags contain 3 clear lavender bags, 1 dotted lavender bag, 5 muted silver bags, 3 plaid purple bags.
dark violet bags contain 2 vibrant beige bags, 3 light crimson bags.
posh lime bags contain no other bags.
dark magenta bags contain 2 muted cyan bags.
striped white bags contain 5 light tan bags, 3 plaid orange bags, 1 dark gold bag, 4 mirrored white bags.
dull cyan bags contain 1 muted red bag, 5 faded lavender bags, 5 plaid gold bags, 5 dark beige bags.
mirrored white bags contain 2 dark olive bags, 4 striped bronze bags.
light plum bags contain 3 wavy crimson bags.
clear red bags contain 4 faded violet bags, 3 dotted tan bags, 1 pale indigo bag, 4 vibrant brown bags.
muted maroon bags contain 3 bright indigo bags, 1 striped magenta bag.
dull chartreuse bags contain 4 posh orange bags.
muted green bags contain 2 vibrant orange bags, 3 dull red bags.
muted coral bags contain 1 dark olive bag, 4 striped bronze bags.
drab brown bags contain 3 shiny maroon bags.
pale teal bags contain 2 faded aqua bags, 4 mirrored magenta bags, 2 plaid red bags, 1 dark coral bag.
dull purple bags contain 2 dotted teal bags, 3 vibrant orange bags.
mirrored maroon bags contain 3 light purple bags, 4 posh beige bags, 1 dim gold bag, 4 striped olive bags.
dull salmon bags contain 3 mirrored red bags.
posh maroon bags contain 3 dark bronze bags, 2 faded lavender bags, 3 plaid red bags.
shiny teal bags contain 1 dotted purple bag, 5 dull black bags, 1 muted purple bag.
dotted olive bags contain 1 wavy aqua bag, 2 clear indigo bags, 2 light coral bags, 1 plaid yellow bag.
drab silver bags contain 2 wavy coral bags, 1 light purple bag, 4 shiny fuchsia bags.
posh lavender bags contain 3 shiny plum bags, 5 wavy coral bags, 2 mirrored green bags.
dark silver bags contain 2 vibrant blue bags, 2 dull crimson bags.
clear indigo bags contain 3 plaid aqua bags, 4 posh orange bags.
plaid purple bags contain 3 vibrant gold bags, 4 wavy fuchsia bags, 2 striped maroon bags, 2 wavy coral bags.
dull gray bags contain 4 striped maroon bags, 1 striped gold bag, 4 vibrant salmon bags, 3 shiny fuchsia bags.
dim maroon bags contain 4 shiny beige bags.
plaid lime bags contain 4 bright lime bags, 5 vibrant tan bags.
faded lime bags contain 3 dotted crimson bags, 2 wavy violet bags.
pale coral bags contain 5 wavy blue bags.
plaid crimson bags contain 2 dull black bags, 3 striped gold bags, 5 dim beige bags, 1 mirrored purple bag.
dark beige bags contain 4 vibrant salmon bags, 2 drab plum bags, 5 dull chartreuse bags, 4 light crimson bags.
clear crimson bags contain 2 shiny fuchsia bags, 5 faded chartreuse bags.
dull orange bags contain 5 plaid bronze bags, 5 faded cyan bags, 3 dotted silver bags, 5 dim purple bags.
dotted black bags contain 2 bright green bags, 5 bright tomato bags, 1 pale magenta bag.
dull coral bags contain 2 dark beige bags, 5 striped gold bags.
vibrant salmon bags contain 5 striped indigo bags, 2 plaid olive bags, 2 drab plum bags.
dim blue bags contain 2 mirrored orange bags.
dim black bags contain 2 light chartreuse bags, 1 wavy fuchsia bag.
dark white bags contain 4 mirrored maroon bags, 2 dim lavender bags, 5 faded yellow bags, 3 dark silver bags.
drab olive bags contain 2 muted white bags, 1 mirrored white bag, 4 striped crimson bags, 4 faded maroon bags.
striped brown bags contain 1 dull fuchsia bag, 1 plaid crimson bag.
clear tomato bags contain 5 drab chartreuse bags.
muted bronze bags contain 3 light magenta bags, 4 clear yellow bags, 5 bright tomato bags.
posh olive bags contain 3 dotted gold bags.
dull maroon bags contain 4 plaid beige bags, 5 drab silver bags, 3 drab lime bags, 5 dull magenta bags.
drab cyan bags contain 3 striped magenta bags, 1 vibrant bronze bag, 2 mirrored green bags, 3 plaid silver bags.
posh magenta bags contain 1 striped chartreuse bag, 4 vibrant silver bags.
muted violet bags contain 4 dark gold bags, 1 posh purple bag, 3 clear purple bags, 4 bright teal bags.
muted silver bags contain 2 bright chartreuse bags, 1 clear chartreuse bag.
wavy coral bags contain 5 mirrored red bags, 1 striped gold bag, 5 faded maroon bags, 1 dark olive bag.
dark green bags contain 3 shiny gold bags.
drab beige bags contain 4 vibrant crimson bags, 4 posh silver bags.
plaid gray bags contain 2 wavy blue bags, 5 dim coral bags.
plaid orange bags contain 3 mirrored orange bags, 1 dark olive bag, 1 light red bag, 2 striped gold bags.
dull silver bags contain no other bags.
shiny lavender bags contain 3 dotted yellow bags, 1 wavy indigo bag, 1 dark coral bag.
dim brown bags contain 4 dim blue bags, 1 drab plum bag.
posh salmon bags contain 3 dim blue bags.
drab orange bags contain 1 faded bronze bag, 5 dull black bags.
wavy crimson bags contain 1 drab salmon bag, 2 vibrant salmon bags.
dull black bags contain 5 vibrant orange bags.
clear teal bags contain 5 faded aqua bags, 1 plaid crimson bag, 1 posh silver bag.
wavy olive bags contain 3 faded aqua bags, 3 faded fuchsia bags, 2 drab cyan bags.
bright gray bags contain 4 clear coral bags, 2 clear white bags, 3 faded lavender bags, 4 dark turquoise bags.
striped green bags contain 1 faded magenta bag, 1 wavy tan bag, 4 posh red bags, 1 striped bronze bag.
clear salmon bags contain 2 striped green bags, 1 striped aqua bag, 3 muted white bags, 3 pale plum bags.
wavy indigo bags contain 2 vibrant orange bags, 1 shiny indigo bag, 1 drab tomato bag.
clear brown bags contain 3 muted maroon bags, 4 dotted silver bags.
vibrant silver bags contain 4 wavy violet bags, 2 posh chartreuse bags.
mirrored salmon bags contain 4 bright brown bags, 3 mirrored crimson bags, 1 mirrored aqua bag.
faded white bags contain 1 wavy crimson bag, 3 drab silver bags, 5 striped yellow bags, 3 dotted olive bags.
muted indigo bags contain 1 wavy indigo bag.
drab aqua bags contain 5 dotted teal bags, 4 mirrored white bags.
posh red bags contain 5 wavy crimson bags.
dim turquoise bags contain 1 striped turquoise bag, 4 dotted crimson bags.
dark yellow bags contain 1 drab olive bag, 3 muted aqua bags.
pale red bags contain 2 vibrant gray bags.
vibrant black bags contain 1 posh gray bag, 5 pale teal bags, 5 shiny red bags.
pale purple bags contain 5 dim olive bags.
dim tomato bags contain 3 plaid lavender bags.
dim yellow bags contain 4 plaid brown bags.
plaid silver bags contain no other bags.
plaid white bags contain 2 muted purple bags, 5 dull black bags.
muted magenta bags contain 2 plaid gray bags, 5 wavy salmon bags, 3 dark chartreuse bags.
bright aqua bags contain 1 dark indigo bag, 1 faded gray bag, 5 vibrant white bags, 2 vibrant gold bags.
drab crimson bags contain 2 clear orange bags.
wavy purple bags contain 2 vibrant plum bags, 3 dark fuchsia bags, 2 pale salmon bags.
wavy teal bags contain 1 drab salmon bag, 4 muted indigo bags, 5 bright violet bags, 5 muted bronze bags.
pale salmon bags contain 5 mirrored blue bags, 4 mirrored maroon bags.
faded lavender bags contain 2 muted blue bags, 4 striped blue bags, 3 pale brown bags, 2 pale purple bags.
dull plum bags contain 5 clear coral bags.
drab maroon bags contain 2 plaid bronze bags, 1 bright orange bag.
light turquoise bags contain 4 striped teal bags, 4 posh indigo bags.
dotted orange bags contain 2 wavy violet bags.
bright teal bags contain 4 clear indigo bags, 1 vibrant violet bag.
mirrored fuchsia bags contain 4 muted brown bags, 5 wavy coral bags, 2 wavy turquoise bags.
dark indigo bags contain 1 light red bag, 4 vibrant lime bags, 2 drab teal bags.
plaid brown bags contain 2 dull gray bags, 3 mirrored magenta bags.
wavy yellow bags contain 4 dotted brown bags.
light orange bags contain 4 shiny black bags.
dark cyan bags contain 3 mirrored chartreuse bags, 4 pale magenta bags, 2 dull black bags, 2 posh lime bags.
muted chartreuse bags contain 3 dull silver bags, 1 dark aqua bag, 2 light tomato bags.
dull red bags contain 5 mirrored orange bags, 2 plaid yellow bags.
dotted cyan bags contain 1 vibrant fuchsia bag, 5 drab olive bags, 4 clear chartreuse bags, 5 pale beige bags.
dim beige bags contain 2 striped yellow bags, 3 bright cyan bags.
dull magenta bags contain 4 faded black bags.
dotted blue bags contain 2 posh maroon bags, 5 dark gold bags.
muted olive bags contain 1 mirrored aqua bag, 4 dull black bags, 5 clear gold bags, 1 mirrored cyan bag.
mirrored silver bags contain 2 bright blue bags, 4 shiny orange bags.
muted brown bags contain 5 muted white bags, 4 clear violet bags, 3 light red bags.
muted lime bags contain 2 plaid yellow bags, 2 pale chartreuse bags, 2 muted tomato bags.
clear silver bags contain 2 clear purple bags, 2 light tomato bags, 4 light gray bags, 1 shiny crimson bag.
dim tan bags contain 2 dull brown bags, 1 dull tomato bag, 2 dim salmon bags, 1 dull green bag.
shiny cyan bags contain 5 plaid turquoise bags.
faded indigo bags contain 4 drab plum bags, 4 clear maroon bags, 5 wavy cyan bags, 4 dim crimson bags.
posh bronze bags contain 5 mirrored olive bags.
posh aqua bags contain 3 dull violet bags, 5 bright silver bags, 1 drab coral bag, 5 shiny orange bags.
dark blue bags contain 5 light silver bags, 1 posh magenta bag, 3 mirrored crimson bags, 4 pale chartreuse bags.
dim crimson bags contain 1 faded gray bag, 3 dull turquoise bags.
dark coral bags contain 3 bright violet bags, 3 mirrored violet bags.
pale green bags contain 2 muted white bags, 5 bright lime bags, 4 dark indigo bags, 2 faded fuchsia bags.
shiny silver bags contain 4 bright teal bags, 1 dim gold bag.
light fuchsia bags contain 1 dull white bag, 1 striped indigo bag, 2 light orange bags.
vibrant crimson bags contain 4 striped maroon bags, 5 dim white bags.
clear yellow bags contain 5 bright green bags.
striped aqua bags contain 4 mirrored beige bags, 4 clear beige bags.
dark chartreuse bags contain 3 bright lime bags, 3 mirrored magenta bags.
wavy turquoise bags contain 4 bright brown bags, 5 mirrored lime bags, 3 pale white bags, 3 drab salmon bags.
faded tomato bags contain 2 clear indigo bags, 3 faded teal bags, 4 dark teal bags.
dull indigo bags contain 5 vibrant indigo bags, 1 mirrored purple bag, 1 vibrant tan bag, 2 shiny plum bags.
posh yellow bags contain 5 clear cyan bags, 3 mirrored red bags, 5 mirrored magenta bags.
plaid yellow bags contain 3 vibrant gold bags, 4 posh crimson bags, 3 mirrored green bags.
plaid olive bags contain 3 vibrant indigo bags, 3 posh indigo bags, 1 posh magenta bag, 5 dim olive bags.
bright cyan bags contain 2 vibrant brown bags, 2 muted red bags.
clear chartreuse bags contain 2 muted salmon bags, 1 plaid aqua bag.
shiny plum bags contain 5 mirrored gray bags, 2 dotted maroon bags.
dim teal bags contain 3 dotted tan bags, 4 faded aqua bags, 2 light teal bags.
mirrored bronze bags contain 3 wavy plum bags, 5 dotted tan bags.
muted turquoise bags contain 2 mirrored silver bags, 2 dotted yellow bags.
clear gold bags contain 4 plaid olive bags.
mirrored orange bags contain 5 mirrored cyan bags, 2 faded maroon bags, 2 bright violet bags.
striped chartreuse bags contain 3 dark gold bags, 2 pale fuchsia bags.
dull turquoise bags contain 5 faded black bags.
bright chartreuse bags contain 1 drab turquoise bag.
vibrant green bags contain 3 wavy plum bags, 1 shiny fuchsia bag, 3 dark yellow bags, 1 dotted lime bag.
mirrored black bags contain 4 plaid red bags, 2 wavy brown bags.
striped magenta bags contain 3 dim lavender bags.
shiny gold bags contain 3 clear fuchsia bags, 2 vibrant indigo bags, 4 dotted maroon bags.
posh fuchsia bags contain 3 dull silver bags, 3 mirrored lime bags, 2 dull black bags.
bright magenta bags contain 5 clear violet bags, 1 light red bag, 1 mirrored white bag.
mirrored tomato bags contain 1 dark olive bag, 5 faded maroon bags.
wavy gray bags contain 5 dotted orange bags, 3 muted magenta bags, 2 plaid maroon bags, 4 drab tomato bags.
dim plum bags contain 4 dim salmon bags, 4 light cyan bags, 3 wavy coral bags.
shiny chartreuse bags contain 2 drab plum bags, 2 pale beige bags.
striped gray bags contain 4 muted aqua bags.
faded cyan bags contain 2 muted coral bags.
clear coral bags contain 5 faded white bags, 5 dull coral bags.
dim violet bags contain 2 dark tomato bags, 3 vibrant silver bags, 2 clear maroon bags.
wavy tomato bags contain 1 striped orange bag, 2 posh magenta bags.
drab chartreuse bags contain 4 posh crimson bags, 3 wavy brown bags.
dotted plum bags contain 4 posh crimson bags, 3 dull magenta bags.
striped crimson bags contain 1 wavy coral bag.
faded yellow bags contain 2 faded gray bags.
faded magenta bags contain 4 dotted yellow bags.
bright orange bags contain 5 dark plum bags, 3 plaid white bags, 3 bright chartreuse bags.
drab red bags contain 4 vibrant cyan bags.
wavy white bags contain 4 mirrored lavender bags, 3 muted tomato bags, 3 faded tomato bags, 5 drab cyan bags.
striped salmon bags contain 5 dotted silver bags.
mirrored violet bags contain 3 plaid silver bags, 1 dotted maroon bag, 5 striped gray bags.
pale fuchsia bags contain 2 dark gold bags.
striped silver bags contain 1 faded cyan bag, 2 muted orange bags.
dull brown bags contain 5 dotted chartreuse bags, 4 vibrant red bags, 2 plaid purple bags, 4 shiny fuchsia bags.
dull gold bags contain 1 dull olive bag, 1 clear coral bag, 4 light tomato bags, 4 muted yellow bags.
plaid green bags contain 5 dark bronze bags, 1 muted aqua bag, 4 plaid aqua bags.
dim white bags contain 4 bright red bags, 2 striped teal bags, 2 posh crimson bags.
drab salmon bags contain no other bags.
dull fuchsia bags contain 5 clear crimson bags, 1 pale green bag, 3 vibrant coral bags, 3 plaid salmon bags.
pale lime bags contain 1 plaid magenta bag.
wavy lavender bags contain 4 faded magenta bags, 3 dark yellow bags, 5 plaid aqua bags.
shiny gray bags contain 4 dark teal bags, 1 wavy crimson bag, 4 posh lime bags.
dull bronze bags contain 5 drab tomato bags, 4 pale tan bags.
dotted chartreuse bags contain 2 dark maroon bags, 4 mirrored black bags, 4 light orange bags.
dotted aqua bags contain 2 mirrored maroon bags, 2 mirrored blue bags, 3 dark cyan bags, 4 dotted olive bags.
striped indigo bags contain 4 mirrored gray bags, 5 light tan bags, 4 dotted tan bags.
shiny magenta bags contain 5 dim chartreuse bags, 2 striped olive bags, 5 clear blue bags.
bright lime bags contain 4 drab cyan bags, 4 striped chartreuse bags, 1 dotted yellow bag.
dotted white bags contain 1 clear purple bag, 1 clear teal bag, 1 dotted cyan bag.
dotted red bags contain 3 dark silver bags.
dotted fuchsia bags contain 1 pale orange bag.
pale aqua bags contain 1 dim beige bag, 2 shiny aqua bags, 1 faded gray bag.
dotted tan bags contain 3 muted coral bags, 1 shiny fuchsia bag, 5 wavy tan bags.
light bronze bags contain 1 drab lavender bag, 5 faded red bags, 3 light tan bags, 1 striped white bag.
dim cyan bags contain 1 vibrant brown bag, 3 faded gray bags, 5 striped lime bags, 5 plaid beige bags.
dim silver bags contain 2 striped gray bags, 3 plaid gold bags, 5 striped orange bags.
shiny aqua bags contain 3 dotted tan bags, 4 muted brown bags, 1 mirrored maroon bag.
drab tan bags contain 4 muted brown bags, 1 dotted lavender bag, 2 dull coral bags.
shiny beige bags contain 2 muted blue bags, 3 wavy turquoise bags, 5 plaid silver bags.
muted aqua bags contain 2 mirrored orange bags.
striped beige bags contain 3 muted coral bags, 4 dim gold bags, 1 dim beige bag.
light teal bags contain 3 faded green bags, 5 dark indigo bags, 1 pale gold bag."""

main_raw_input = main_raw_input.splitlines()

def create_data_structure(initial_data):
    result = {}

    for item in initial_data:
        bag_and_contents_regex = r"^(\w+ \w+) bags contain (.*)"
        bag_and_contents = re.search(bag_and_contents_regex, item)
        bag_type = bag_and_contents[1]

        contents_string = bag_and_contents[2][:-1]  # [:-1] removes trailing period
        contents_regex = r"([0-9] )*(\w+ \w+) bag"
        contents_tuples = re.findall(contents_regex, contents_string)

        bag_contents = []
        for contents_tuple in contents_tuples:
            if contents_tuple[1] != "no other":
                bag_contents.append({
                    "count": int(contents_tuple[0]),
                    "type": contents_tuple[1]
                })

        result[bag_type] = bag_contents

    return result



newData = parseNewData()
total = recursionPartTwo(newData,'shiny gold')
print(total)

