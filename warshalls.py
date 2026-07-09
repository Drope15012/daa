def warshall(g):
    n = len(g)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = g[i][j] or (g[i][k] and g[k][j])
    return g

g = [
    [1,1,0],
    [0,1,1],
    [0,0,1]
]

ans = warshall(g)

for i in ans:
    print(i)
