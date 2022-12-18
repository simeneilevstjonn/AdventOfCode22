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

cumulativeMax = 0
queue = []

# Queue entry format: [vertex, time, flow, cumulative, opened]

queue.append([graph["AA"], 30, 0, 0, []])

while len(queue):
    vertex, time, flow, cumulative, opened = queue.pop(0)

    print(len(queue))

    if time < 1:
        cumulativeMax = max(cumulative, cumulativeMax)
        continue

    for e in vertex.edges:
        # Push directly
        queue.append([graph[e], time - 1, flow, cumulative + flow, opened[::]])

        # If the current valve is not opened
        if vertex not in opened and vertex.flow != 0:
            queue.append([graph[e], time - 2, flow + vertex.flow, cumulative + flow * 2 + vertex.flow, opened[::] + [vertex]])

print(cumulativeMax)
