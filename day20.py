class EncryptedCoordinateNumber:
    def __init__(self, number):
        self.number = int(number)

data = list(map(EncryptedCoordinateNumber, open("data20.txt", "r").read().split("\n")))

cpy = data[::]

l = len(data)

#print(*map(lambda x : x.number, data))
#print()

for n in cpy:
    #print("Active", n.number)
    i = -1
    for j in range(len(data)):
        if data[j].number == n.number:
            i = j
            break

    #data[i], data[(i + n.number) % l] = data[(i + n.number) % l], data[i]

    sign = n.number // abs(n.number) if n.number != 0 else 0

    for j in range(abs(n.number)):
        data[(i + sign * j) % l], data[(i + sign * (j + 1)) % l] = data[(i + sign * (j + 1)) % l], data[(i + sign * j) % l]


    #print(*map(lambda x : x.number, data))

    #print()


idx = -1
for i in range(len(data)):
    if data[i].number == 0:
        idx = i
        break

s = sum(data[(idx + i * 1000) % l].number for i in [1, 2, 3])

#print(*map(lambda x : x.number, data))

print(s)