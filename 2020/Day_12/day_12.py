f = open('input.txt')
data = f.readlines()
partOne = False

newData = []
for i in data:
    if '\n' in i:
        newData.append(i[:-1])
    else:
        newData.append(i)
def turnLeft(direction,degree):
    d=direction-degree
    if d <= 0:
        d = abs(d%360)
    return d
def turnRight(direction,degree):
    d=direction+degree
    if d >= 360:
        d = d%360
    return d
def instructions():
    direction = 90
    xValue = 0
    yValue=0
    for i in newData:
        if i[0] == 'N':
            yValue+=(int(i[1:]))
        elif i[0] == 'S':
            yValue-=(int(i[1:]))
        elif i[0] == 'E':
            xValue+=(int(i[1:]))
        elif i[0] == 'W':
            xValue-=(int(i[1:]))
        elif i[0] == 'R':
            direction = turnRight(direction,int(i[1:]))
        elif i[0] == 'L':
            direction = turnLeft(direction,int(i[1:]))
        else:
            if direction == 0:
                yValue += (int(i[1:]))
            elif direction == 180:
                yValue -= (int(i[1:]))
            elif direction == 90:
                xValue += (int(i[1:]))
            else:
                xValue -= (int(i[1:]))
    return abs(xValue)+abs(yValue)

print(instructions())


