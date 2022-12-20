

f = open("/Users/davidfan/Desktop/Work/Leetcode/Advent/2022/day_1/input.txt", "r")
data = f.read()

tokens = data.split('\n')

calCounts = []

count = 0
for i in tokens:
    if i == '':
        calCounts.append(count)
        count = 0
    else:
        count += int(i)
        
calCounts.sort(reverse = True)
print(calCounts[0] + calCounts[1] + calCounts[2])

    