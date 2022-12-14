data = [[(int(j.split(",")[1]), int(j.split(",")[0])) for j in i.split("->")] for i in open("data14.txt","r").read().split("\n")]

minx = 500
maxx = 500
miny = 0
maxy = 0

for i in data:
    for j in i:
        minx = min(minx, j[1])
        maxx = max(maxx, j[1])
        miny = min(miny, j[0])
        maxy = max(maxy, j[0])

# Create a matrix of minimum size with one in padding in all directions
matrix = [[i == maxy + 2] * 1000 for i in range(maxy + 3)]

for line in data:
    for i in range(1, len(line)):
        y0,x0 = line[i - 1]
        y1,x1 = line[i]

        if y0 == y1:
            if x0 < x1:
                for j in range(x0, x1 + 1):
                    matrix[y0][j] = True
            else:
                for j in range(x1, x0 + 1):
                    matrix[y0][j] = True
        elif x0 == x1:
            if y0 < y1:
                for j in range(y0, y1 + 1):
                    matrix[j][x0] = True
            else:
                for j in range(y1, y0 + 1):
                    matrix[j][x0] = True

def sandmulate(y, x, matrix):
    # Space below
    if not matrix[y + 1][x]:
        return sandmulate(y + 1, x, matrix)
    # Space below left
    elif not matrix[y + 1][x - 1]:
        return sandmulate(y + 1, x - 1, matrix)
    # Space below right
    elif not matrix[y + 1][x + 1]:
        return sandmulate(y + 1, x + 1, matrix)
    # Settle
    else:
        matrix[y][x] = True
        return True

i = 0
while not matrix[0][500]:
    sandmulate(0, 500, matrix)
    i += 1

print(i)