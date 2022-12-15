import re

data = [list(map(int, re.findall("-*\d+", i))) for i in open("data15.txt", "r").read().split("\n")]

blx = [i[2] for i in data if i[3] == 2000000]

inside = lambda sx, sy, px, py, cx, cy : abs(px - sx) + abs(py - sy) >= abs(cx - sx) + abs(cy - sy)

ins = []
for sx, sy, px, py in data:
    for i in range(sx - abs(sx - px) - abs(sy - py) - 10, sx + abs(sx - px) + abs(sy - py) + 10):
        if i not in blx and inside(sx, sy, px, py, i, 2000000):ins.append(i)


print(len(set(ins)))