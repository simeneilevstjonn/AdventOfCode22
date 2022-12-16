raw = open("data16.txt", "r").read().split("\n")

class Node:
    def __init__(self, id, flow, graph, edges):
        self.id = id
        self.flow = flow
        self.graph = graph
        self.edges = edges

graph = {}

for i in raw:
    i = i.replace("tunnel ", "tunnels ").replace("valve ", "valves ").replace("leads ", "lead ")
    a,b = i.split("; tunnels lead to valves ")
    edges = b.split(", ")
    id = a[6:8]
    flow = int(a.split("=")[1])

    graph[id] = Node(id, flow, graph, edges)

flowRate = 0
cumulativeFlow = 0
active = graph["AA"]
i = 0

while i < 30:
    # Open this node's valve if has a grater flow than any of its neighbours
    # Find neightbour with max flow
    bestNb = max([graph[id] for id in active.edges], key=lambda x : x.flow)

    if bestNb.flow <= active.flow:
        flowRate += active.flow
        active.flow = 0
        i += 1
        cumulativeFlow += flowRate

    active = bestNb
    i += 1
    cumulativeFlow += flowRate
    
print(cumulativeFlow)