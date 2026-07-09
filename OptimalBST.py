def obst(p, n):
    C = [[0]*(n+2) for _ in range(n+2)]
    R = [[0]*(n+2) for _ in range(n+2)]

    for i in range(1, n+1):
        C[i][i], R[i][i] = p[i], i

    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            s = sum(p[i:j+1])
            C[i][j] = min((C[i][k-1] + C[k+1][j] + s, k) for k in range(i, j+1))
            C[i][j], R[i][j] = C[i][j]

    return C, R

n = int(input("Keys: "))
p = [0] + list(map(float, input("Probabilities: ").split()))

C, R = obst(p, n)

print("Minimum Cost:", C[1][n])
