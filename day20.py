class EncryptedCoordinateNumber:
    def __init__(self, number):
        self.number = int(number)

data = list(map(EncryptedCoordinateNumber, open("testdata20.txt", "r").read().split("\n")))

cpy = data[::]

l = len(data)

print(*map(lambda x : x.number, data))
print()

for n in cpy:
    print("Active", n.number)
    i = -1
    for j in range(len(data)):
        if data[j].number == n.number:
            i = j
            break

    #data[i], data[(i + n.number) % l] = data[(i + n.number) % l], data[i]

    data.pop(i)

    data.insert((i + n.number) % l, n)


    print(*map(lambda x : x.number, data))

    print()


idx = -1
for i in range(len(data)):
    if data[i].number == 0:
        idx = i
        break

s = sum(data[(idx + i * 1000) % l].number for i in [1, 2, 3])

print(*map(lambda x : x.number, data))

print(s)