import sys

sys.setrecursionlimit(10**6)

points = [list(map(int, i.split(","))) for i in open("data18.txt", "r").read().split("\n")]

size = max([max(i) for i in points]) + 1

space = [[[False] * size for i in range(size)] for j in range(size)]
visited = [[[False] * size for i in range(size)] for j in range(size)]


for x, y, z in points:
    space[z][y][x] = True

area = 0

queue = [[0, 0, 0]]

while len(queue):
    z, y, x = queue.pop(0)

    if visited[z][y][x]:
        continue

    if space[z][y][x]:
        area += 1
        continue
    
    if x != 0:
        queue.append([z, y, x - 1])
    if y != 0:
        queue.append([z, y - 1, x])
    if z != 0:
        queue.append([z - 1, y, x])
    if x != size - 1:
        queue.append([z, y, x + 1])
    if y != size - 1:
        queue.append([z, y + 1, x])
    if z != size - 1:
        queue.append([z + 1, y, x])

print(area)