data = [[i.split()[0], int(i.split()[1])] for i in open("testdata9.txt","r").read().split("\n")]
rope = [[0,0] for _ in range(10)]
tailvisits = []

for direction, distance in data:
    for _ in range(distance):
        if direction == "U":
            rope[0][0] += 1
        elif direction == "D":
            rope[0][0] -= 1
        elif direction == "L":
            rope[0][1] -= 1
        elif direction == "R":
            rope[0][1] += 1
        
        # Move tail if not adjacent. Eucledean distance above sqrt(2)
        for i in range(1,10):
            if (rope[i][0] - rope[i - 1][0])**2 + (rope[i][1] - rope[i - 1][1])**2 > 2:
                rope[i][0] += (rope[i - 1][0] > rope[i][0]) - (rope[i - 1][0] < rope[i][0])
                rope[i][1] += (rope[i - 1][1] > rope[i][1]) - (rope[i - 1][1] < rope[i][1])

            # Add tails position
            tailvisits.append((rope[9][0], rope[9][1]))

print(len(set(tailvisits)))
