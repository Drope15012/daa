def mm(a, l, h):
    if l == h: return a[l], a[l]
    if h == l+1: return (a[l], a[h]) if a[l] < a[h] else (a[h], a[l])
    m = (l+h)//2
    x1, y1 = mm(a, l, m)
    x2, y2 = mm(a, m+1, h)
    return min(x1, x2), max(y1, y2)

a = [12, 45, 7, 23, 56, 3, 89]
mn, mx = mm(a, 0, len(a)-1)

print("Min:", mn)
print("Max:", mx)
