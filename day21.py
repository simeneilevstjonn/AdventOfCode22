class Node:
    def __init__(self, data, tree):
        if data.isnumeric():
            self.val = int(data)
            self.op = None
            self.left = None
            self.right = None
        else:
            self.left = data[:4]
            self.right = data[7:]
            self.op = data[5]
            self.val = None
        self.tree = tree
    
    def value(self):
        if self.val is not None:
            return self.val
        
        return eval(f"{self.tree[self.left].value()} {self.op} {self.tree[self.right].value()}")


tree = {}

for x in open("data21.txt", "r").read().split("\n"):
    id, data = x.split(": ")
    tree[id] = Node(data, tree)

print(tree["root"].value())