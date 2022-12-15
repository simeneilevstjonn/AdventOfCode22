import re

data = [list(map(int, re.findall("-*\d+", i))) for i in open("data15.txt", "r").read().split("\n")]

inside = lambda sx, sy, px, py, cx, cy : abs(px - sx) + abs(py - sy) == abs(cx - sx) + abs(cy - sy)

count = 0
for i in range(-10**10, 10**10):
    if i % 10**8 == 0:
        print(i)
    for sx, sy, px, py in data:
        if px == i:
            break
        count += inside(sx, sy, px, py, i, 2000000)

print(count)