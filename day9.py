data = [[i.split()[0], int(i.split()[1])] for i in open("data9.txt","r").read().split("\n")]
head = [0, 0]
tail = [0, 0]
tailvisits = []

for direction, distance in data:
    for _ in range(distance):
        if direction == "U":
            head[0] += 1
        elif direction == "D":
            head[0] -= 1
        elif direction == "L":
            head[1] -= 1
        elif direction == "R":
            head[1] += 1
        
        # Move tail if not adjacent. Eucledean distance above sqrt(2)
        if (tail[0] - head[0])**2 + (tail[1] - head[1])**2 > 2:
            tail[0] += (head[0] > tail[0]) - (head[0] < tail[0])
            tail[1] += (head[1] > tail[1]) - (head[1] < tail[1])
            

        # Add tails position
        tailvisits.append((tail[0], tail[1]))

print(len(set(tailvisits)))
