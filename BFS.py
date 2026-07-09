from collections import deque

g = {}
for _ in range(int(input("No. of vertices: "))):
    g[input("Vertex: ")] = input("Neighbors: ").split()

s = input("Start vertex: ")

q = deque([s])
v = {s}

while q:
    x = q.popleft()
    print(x, end=" ")
    for i in g[x]:
        if i not in v:
            v.add(i)
            q.append(i)
