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

def turnLeft2(x,y,degree):
    if degree%360 == 90:
        tempY = y
        y = x
        x = -tempY
    elif degree % 360 == 180:
        y = -y
        x = -x
    elif degree % 360 == 270:
        x,y = turnRight2(x,y,90)
    return x,y


def turnRight2(x,y,degree):
    if degree%360 == 90:
        tempX = x
        x = y
        y = -tempX
    elif degree % 360 == 180:
        y = -y
        x = -x
    elif degree % 360 == 270:
        x,y = turnLeft2(x,y,90)
    return x,y

def instructions2():
    xValue = 0
    yValue=0
    wayPointX = 10
    wayPointY = 1
    for i in newData:
        if i[0] == 'N':
            wayPointY+=(int(i[1:]))
        elif i[0] == 'S':
            wayPointY-=(int(i[1:]))
        elif i[0] == 'E':
            wayPointX+=(int(i[1:]))
        elif i[0] == 'W':
            wayPointX-=(int(i[1:]))
        elif i[0] == 'R':
            wayPointX,wayPointY = turnRight2(wayPointX,wayPointY,int(i[1:]))
        elif i[0] == 'L':
            wayPointX,wayPointY = turnLeft2(wayPointX,wayPointY,int(i[1:]))
        else:
            numTies = int(i[1:])
            xValue+=wayPointX*numTies
            yValue+=wayPointY*numTies
    return abs(xValue)+abs(yValue)

print(instructions())
print(instructions2())


