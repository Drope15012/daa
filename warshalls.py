n = int(input("Vertices: "))
g = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] |= g[i][k] & g[k][j]

print("Transitive Closure:")
for r in g:
    print(*r)
