elves = []

for i, x in enumerate(open("data23.txt", "r").read().split("\n")):
    for j, y in enumerate(x):
        if y == "#":
            elves.append((i, j))



for i in range(10):
    proplocs = []

    for y, x in elves:
        l = len(proplocs)

        # No move
        if (y + 1, x) not in elves and (y + 1, x + 1) not in elves and (y + 1, x - 1) not in elves and (y, x + 1) not in elves and (y, x - 1) not in elves and (y - 1, x) not in elves and (y - 1, x - 1) not in elves and (y - 1, x + 1) not in elves:
            proplocs.append((y, x))
        else:
            for j in range(4):
                d = (j + i) % 4

                # North
                if d == 0 and (y - 1, x) not in elves and (y - 1, x + 1) not in elves and (y - 1, x - 1) not in elves:
                    proplocs.append((y - 1, x))
                    break
                # South
                elif d == 1 and (y + 1, x + 1) not in elves and (y + 1, x - 1) not in elves and (y + 1, x) not in elves:
                    proplocs.append((y + 1, x))
                    break
                # West
                elif d == 2 and (y, x - 1) not in elves and (y + 1, x - 1) not in elves and (y - 1, x - 1) not in elves:
                    proplocs.append((y, x - 1))
                    break
                # East
                elif d == 3 and (y, x + 1) not in elves and (y + 1, x + 1) not in elves and (y - 1, x + 1) not in elves:
                    proplocs.append((y, x + 1))
                    break
            
            # In case no location has been proposed. (Though this might not ever happen)
            if len(proplocs) == l:
                proplocs.append((y, x))
    
    # Move to the proposed locations
    for i, l in enumerate(proplocs):
        if proplocs.count(l) == 1:
            elves[i] = l

may = max(elves, key=lambda x : x[0])[0]
miy = min(elves, key=lambda x : x[0])[0]
maX = max(elves, key=lambda x : x[1])[1]
mix = min(elves, key=lambda x : x[1])[1]

print((may - miy + 1) * (maX - mix + 1) - len(elves))