class Monkey:
    def __init__(self):
        self.total = 0
        self.queue = []
        self.monkeys = []
        self.ifFalse = -1
        self.ifTrue = -1
        self.mod = -1
        self.operation = None

    def inspect(self):
        for item in self.queue:
            item = self.operation(item)
            item //= 3
            if item % self.mod:
                self.monkeys[self.ifFalse].queue.append(item)
            else:
                self.monkeys[self.ifTrue].queue.append(item)
        self.total += len(self.queue)
        self.queue = []

raw = open("data11.txt","r").read().split("\n\n")

monkeys=[]

for data in raw:
    data = data.split("\n")
    m = Monkey()
    m.queue = list(map(int, data[1][18:].split(",")))
    m.operation = lambda old : eval(data[2][19:])
    m.mod = int(data[3][21:])
    m.ifTrue = int(data[4][29:])
    m.ifFalse = int(data[5][30:])
    m.monkeys = monkeys

    monkeys.append(m)


for i in range(20):
    for m in monkeys:
        m.inspect()
    
monkeys.sort(key=lambda x : x.total)
print(monkeys[-1].total * monkeys[-2].total)