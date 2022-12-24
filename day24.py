import heapq

grid = [[j for j in i] for i in open("data24.txt", "r").read().split("\n")]

blizzards = []

for i, y in enumerate(grid):
    for j, x in enumerate(y):
        if x == "<":
            blizzards.append((i, j, 27))
        elif x == ">":
            blizzards.append((i, j, 9))
        elif x == "v":
            blizzards.append((i, j, 18))
        elif x == "^":
            blizzards.append((i, j, 0))

blizzardList = [blizzards]

def blizzard(n):
    while len(blizzardList) - 1 < n:
        blizzardList.append(blizzardInc(blizzardList[-1]))

    return blizzardList[n]

def blizzardInc(blzards):
    new = []

    for y, x, hdg in blzards:
        ny = y
        nx = x

        if hdg == 0:
            ny -= 1
        elif hdg == 9:
            nx += 1
        elif hdg == 18:
            ny += 1
        elif hdg == 27:
            nx -= 1
        
        if grid[ny][nx] == "#":
            new.append((y, x, (hdg + 18) % 36))
        else:
            new.append((ny, nx, hdg))
    
    return new

def blizzardContains(n, y, x):
    blzards = blizzard(n)

    for by, bx, h in blzards:
        if by == y and bx == x:
            return True
    
    return False

distance = [[2147483647] * len(i) for i in grid]
visited = [[False] * len(i) for i in grid]

distance[0][1] = 0

class GridCoordinate:
    def __init__(self, y, x):
        self.y = y
        self.x = x
    def dist(self):
        global distance
        return distance[self.y][self.x]
    def __lt__(self, a):
        return self.dist() < a.dist()
    
queue = [GridCoordinate(0, 1)]

while queue:
    c = heapq.heappop(queue)

    y, x = c.y, c.x

    visited[y][x] = True

    # Each child
    children = [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]

    for cy, cx in children:
        if grid[cy][cx] != "#" and not visited[cy][cx] and not blizzardContains(c.dist() + 1, cy, cx):
            distance[cy][cx] = c.dist() + 1
            heapq.heappush(queue, GridCoordinate(cy, cx))

print(distance[-1][-2])