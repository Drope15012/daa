n = 4
x = [0] * n

def safe(r, c):
    return all(x[i] != c and abs(x[i] - c) != abs(i - r) for i in range(r))

def solve(r):
    if r == n:
        for i in range(n):
            print(*["Q" if x[i] == j else "." for j in range(1, n + 1)])
        print()
        return
    for c in range(1, n + 1):
        if safe(r, c):
            x[r] = c
            solve(r + 1)

solve(0)
