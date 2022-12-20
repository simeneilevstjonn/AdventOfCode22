class EncryptedCoordinateNumber:
    def __init__(self, number):
        self.number = int(number)

data = list(map(EncryptedCoordinateNumber, open("data20.txt", "r").read().split("\n")))

cpy = data[::]

l = len(data)

for n in cpy:
    i = data.index(n)

    data[i], data[(i + n.number) % l] = data[(i + n.number) % l], data[i]


idx = -1
for i in range(len(data)):
    if data[i].number == 0:
        idx = i
        break

s = sum(data[(idx + i * 1000) % l].number for i in [1, 2, 3])

print(s)