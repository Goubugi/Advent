f = open('input.txt')
data = f.readlines()
p1 = False

h = 0
d = 0
a = 0

if (p1):
    for command in data:
        step = [int(s) for s in command.split() if s.isdigit()][0]
        if "forward" in command:
            h += step
        elif "down" in command:
            d += step
        elif "up" in command:
            d -= step
    print(f"Horizontal is {h} and Depth is {d}, answer is {h * d}")
else:
    for command in data:
        step = [int(s) for s in command.split() if s.isdigit()][0]
        if "forward" in command:
            h += step
            d += a*step
        elif "down" in command:
            a += step
        elif "up" in command:
            a -= step
    print(f"Horizontal is {h} and Depth is {d}, answer is {h * d}")

