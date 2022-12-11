class Monkey:
    def __init__(self):
        self.total = 0
        self.queue = []
        self.monkeys = []
        self.ifFalse = -1
        self.ifTrue = -1
        self.mod = -1
        self.operation = None
        self.id = -1
        self.gmod = -1

    def inspect(self):
        for item in self.queue:
            #print("Monkey", self.id, "inspects item", item)
            old = item
            item = eval(self.operation)

            #print("After op", item)
            item %= self.gmod
            #print("After div", item)
            if item % self.mod == 0:
                #print("Div by", self.mod, "pass to", self.ifTrue)
                self.monkeys[self.ifTrue].queue.append(item)
            else:
                #print("Not div by", self.mod, "pass to", self.ifFalse)
                self.monkeys[self.ifFalse].queue.append(item)
        self.total += len(self.queue)
        #print("Inc count by", len(self.queue))
        #print()
        self.queue = []

raw = open("data11.txt","r").read().split("\n\n")

monkeys=[]
i = 0

for data in raw:
    data = data.split("\n")
    m = Monkey()
    m.queue = list(map(int, data[1][18:].split(",")))
    m.operation = data[2][19:]
    m.mod = int(data[3][21:])
    m.ifTrue = int(data[4][29:])
    m.ifFalse = int(data[5][30:])
    m.id = i
    i += 1
    m.monkeys = monkeys

    monkeys.append(m)

globmod = 1
for m in monkeys:
    globmod *= m.mod

for m in monkeys:
    m.gmod = globmod


for i in range(10000):
    print("Round begin", i)
    for m in monkeys:
        m.inspect()
    #print()


monkeys.sort(key=lambda x : x.total)
print(monkeys[-1].total * monkeys[-2].total)