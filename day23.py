elves = []
matrix = [[False] * 2000 for _ in range(2000)]

for i, x in enumerate(open("data23.txt", "r").read().split("\n")):
    for j, y in enumerate(x):
        if y == "#":
            elves.append((i, j))
            matrix[i + 1000][j + 1000] = True

m = lambda y, x : not matrix[y + 1000][x + 1000]


i = 0
while True:
    proplocs = []

    for y, x in elves:
        l = len(proplocs)

        # No move
        if m(y + 1, x) and m(y + 1, x + 1) and m(y + 1, x - 1) and m(y, x + 1) and m(y, x - 1) and m(y - 1, x) and m(y - 1, x - 1) and m(y - 1, x + 1):
            proplocs.append((y, x))
        else:
            for j in range(4):
                d = (j + i) % 4

                # North
                if d == 0 and m(y - 1, x) and m(y - 1, x + 1) and m(y - 1, x - 1):
                    proplocs.append((y - 1, x))
                    break
                # South
                elif d == 1 and m(y + 1, x + 1) and m(y + 1, x - 1) and m(y + 1, x):
                    proplocs.append((y + 1, x))
                    break
                # West
                elif d == 2 and m(y, x - 1) and m(y + 1, x - 1) and m(y - 1, x - 1):
                    proplocs.append((y, x - 1))
                    break
                # East
                elif d == 3 and m(y, x + 1) and m(y + 1, x + 1) and m(y - 1, x + 1):
                    proplocs.append((y, x + 1))
                    break
            
            # In case no location has been proposed. (Though this might not ever happen)
            if len(proplocs) == l:
                proplocs.append((y, x))
    
    moved = 0

    # Move to the proposed locations
    for j, l in enumerate(proplocs):
        if proplocs.count(l) == 1 and l != elves[j]:
            y0, x0 = elves[j]
            matrix[y0 + 1000][x0 + 1000] = False
            elves[j] = l
            y, x = l
            matrix[y + 1000][x + 1000] = True
            moved += 1


    if moved == 0:
        break

    i += 1

print(i + 1)