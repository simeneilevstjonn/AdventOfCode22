sequence = [i == ">" for i in open("data17.txt", "r").read()]

matrix = []

def height():
    for i in range(len(matrix)):
        if sum(matrix[i]) == 0:
            return i
    return len(matrix)

def fitRock(coords, rock):
    # Coords is the bottom-right of the rock. This is the highest x and lowest y in the shape. This starts as (y, x) (h + 3, 4)
    # Rock is specified dimensionally equal to matrix. The top of the rock is at the highest y. The right is at the highest x.

    # Start by testing if the horizontal movement is possible
    if sequence.pop():
        # Left movement
        # Hits wall if x + 1 is 7
        if coords[1] + 1 != 7:
            allow = True
            # Test each row
            for y in range(len(rock)):
                for x in range(len(rock[0])):
                    # The y would be coords y + y.
                    # The x would be coords x + x - len rock[0] + 2
                    if rock[y][x] and matrix[coords[0] + y][coords[1] + x + 2 - len(rock[0])]:
                        allow = False
                        break

            if allow:
                coords = (coords[0], coords[1] + 1)    
    else:
        # Right movement
        # Hits wall if x - len rock[0] is 0
        if coords[1] - len(rock[0]) != 0:
            allow = True
            # Test each row
            for y in range(len(rock)):
                for x in range(len(rock[0])):
                    # The y would be coords y + y.
                    # The x would be coords x + x - len rock[0]
                    if rock[y][x] and matrix[coords[0] + y][coords[1] + x - len(rock[0])]:
                        allow = False
                        break

            if allow:
                coords = (coords[0], coords[1] - 1)

    # Test the possibility of downward movement
    if coords[0] != 0:
        allow = True
        # Test each row
        for y in range(len(rock)):
            for x in range(len(rock[0])):
                # The y would be coords y + y - 1.
                # The x would be coords x + x - len rock[0] + 1
                if rock[y][x] and matrix[coords[0] + y - 1][coords[1] + x + 1 - len(rock[0])]:
                    allow = False
                    break

        if allow:
            coords = (coords[0] - 1, coords[1])
            return fitRock(coords, rock)

    # Fit the rock
    for y in range(len(rock)):
        for x in range(len(rock[0])):
            # The y would be coords y + y.
            # The x would be coords x + x - len rock[0] + 1
            if rock[y][x]: matrix[coords[0] + y][coords[1] + x + 1 - len(rock[0])] = True

rocks = [
    [[True, True, True, True]],
    [[False, True, False], [True, True, True], [False, True, False]],
    [[True, True, True], [False, False, True], [False, False, True]],
    [[True], [True], [True], [True]],
    [[True, True], [True, True]]
]

for i in range(2022):
    # Coords start as (y, x) (h + 3, 4)
    # Make sure that there are 7 available rows
    while len(matrix) - height() < 7:
        matrix.append([False] * 7)
    
    # Simulate the rock
    fitRock((height() + 3, 4), rocks[i % 5])

print(height())