points = [list(map(int, i.split(","))) for i in open("data18.txt", "r").read().split("\n")]
area = 0

for x, y, z in points:
    area += [x, y, z + 1] not in points
    area += [x, y, z - 1] not in points
    area += [x, y + 1, z] not in points
    area += [x, y - 1, z] not in points
    area += [x + 1, y, z] not in points
    area += [x - 1, y, z] not in points

print(area)