grid = [[j for j in i] for i in open("data12.txt","r").read().split("\n")]

start = None
end = None

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "S":
            start = (y, x)
            grid[y][x] = "a"
        elif grid[y][x] == "E":
            end = (y, x)
            grid[y][x] = "z"

weight = [[1e100 for i in range(len(grid[0]))] for j in range(len(grid))]
vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

weight[start[0]][start[1]] = 0

queue = [start]

while len(queue):
    y, x = queue.pop()

    if not vis[y][x]:
        edge = ([(y - 1, x)] if y != 0 else []) + ([(y + 1, x)] if y != len(grid) - 1 else []) + ([(y, x - 1)] if x != 0 else []) + ([(y, x + 1)] if x != len(grid[0]) - 1 else [])

        for a, b in edge:
            if ord(grid[a][b]) - 1 <= ord(grid[y][x]):
                weight[a][b] = min(weight[a][b], weight[y][x] + 1)
                queue.append((a, b))

        vis[y][x] = True


print(weight[end[0]][end[1]])