INF = 99999

n = int(input("Vertices: "))
e = int(input("Edges: "))

d = [[0 if i == j else INF for j in range(n)] for i in range(n)]

print("Enter u v w:")
for _ in range(e):
    u, v, w = map(int, input().split())
    d[u][v] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

for r in d:
    print(*["INF" if x == INF else x for x in r])
