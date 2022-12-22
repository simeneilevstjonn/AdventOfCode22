import re

rgrid, rseq = open("data22.txt", "r").read().split("\n\n")

seq = re.findall("\d+|[R,L]", rseq)

grid = [[j for j in i] for i in rgrid.split("\n")]

hdg = 0
y = 0
x = -1

sy = len(grid)
sx = len(grid[0])

for i in range(len(grid[0])):
    if grid[0][i] == ".":
        x = i
        break

for instruct in seq:
    # Turning
    if instruct == "R":
        hdg = (hdg + 1) % 4
        continue
    elif instruct == "L":
        hdg = (hdg - 1) % 4
        continue

    steps = int(instruct)
    
    for j in range(steps):
        # Find the next point
        # Right
        if hdg == 0:
            i = 1
            while grid[y][(x + i) % sx] == " ":
                i += 1
            
            nx = (x + i) % sx
            # Check if wall
            if grid[y][nx] == "#":
                break
            
            x = nx
        # Left
        elif hdg == 2:
            i = 1
            while grid[y][(x - i) % sx] == " ":
                i += 1
            
            nx = (x - i) % sx
            # Check if wall
            if grid[y][nx] == "#":
                break
            
            x = nx
        # Down
        elif hdg == 1:
            i = 1
            while grid[(y + i) % sy][x] == " ":
                i += 1
            
            ny = (y + i) % sy
            # Check if wall
            if grid[ny][x] == "#":
                break
            
            y = ny
        # Up
        elif hdg == 3:
            i = 1
            while grid[(y - i) % sy][x] == " ":
                i += 1
            
            ny = (y - i) % sy
            # Check if wall
            if grid[ny][x] == "#":
                break
            
            y = ny

print(1000 * (y + 1) + 4 * (x + 1) + hdg)
    