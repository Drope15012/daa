def search(t, p):
    b = {c:i for i, c in enumerate(p)}
    m, n, s = len(p), len(t), 0

    while s <= n-m:
        j = m-1
        while j >= 0 and p[j] == t[s+j]:
            j -= 1
        if j < 0:
            print("Pattern found at", s)
            s += m - b.get(t[s+m], -1) if s+m < n else 1
        else:
            s += max(1, j - b.get(t[s+j], -1))

text = input("Text: ")
pat = input("Pattern: ")
search(text, pat)
