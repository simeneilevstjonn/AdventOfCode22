import sys

sys.setrecursionlimit(10**6)

points = [list(map(int, i.split(","))) for i in open("data18.txt", "r").read().split("\n")]

size = max([max(i) for i in points]) + 1

space = [[[False] * size for i in range(size)] for j in range(size)]
visited = [[[False] * size for i in range(size)] for j in range(size)]


for x, y, z in points:
    space[z][y][x] = True

area = 0

def dfs(z, y, x):
    if visited[z][y][x]:
        return
    
    if space[z][y][x]:
        global area
        area += 1
        return
    
    if x != 0:
        dfs(z, y, x - 1)
    if y != 0:
        dfs(z, y - 1, x)
    if z != 0:
        dfs(z - 1, y, x)
    if x != size - 1:
        dfs(z, y, x + 1)
    if y != size - 1:
        dfs(z, y + 1, x)
    if z != size - 1:
        dfs(z + 1, y, x)

dfs(0,0,0)

print(area)